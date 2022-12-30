from luxtronik import Luxtronik
from flask import Flask, make_response
import yaml

# read metrics file
with open ('metric.yml', 'r') as file:
    data = yaml.safe_load(file)

app = Flask(__name__)

@app.route('/metrics')
def metrics():    
    # connect to heatpump
    heatpump = Luxtronik('192.168.2.5', 8889)
    metric_text = ""
    for metric in data['metrics']: 
        value = heatpump.calculations.get(metric['key'])
        metric_text += "# TYPE {0} {1}\n".format(metric['name'], metric['type'])
        metric_text += "{0} {1}\n".format(metric['name'], value)
    response = make_response(metric_text)
    response.headers['Content-Type'] = "text/plain; version-0.0.4"
    return response