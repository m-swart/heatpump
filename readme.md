# Milans personal project


## Introduction
The MYP personal project is a long term project held in grade 10. In the project, we should explore something which inspires or intrests us. My learning goal of this project is to program and be able to process, analyse/ draw conclusions from data. Furthermore would I like to test my learning goal by creating a program which is able to store the data from my home heat pump, creating dashboards from the data and by writing a short report analysing the trends that can be derived from the dashboards.

I have chosen to upload the program and its documentation on Github, because it is serves as evidence and it is easy to explain the program using this platform. Furthermore can it be useful for others, whom perphaps want to observe their heatpump's performance.

This pages describes the general working of my program. The [analysis page](./analysis.md) contains my observations regarding the data I collected.

## About heatpumps
The heatpump is the source of data for my dashboards and the device my program had to collect data from. 

A heatpump extracts heat from a cold source (air or ground) to a warm space, making the cool source cooler and the warm space, our houses, warmer. This is the reverse process of an air conditioner. To optimize this process, the heatpumps are installed with sensors, measuring metrics such as outside temperature. These metrics are used to predict how much energy is needed to heat the house. 

The heatpump is able to do this because it has its own little computer, also known as 'controller'. My program (Prometheus exporter) is communciating with this communicating with this heat pump controller to retrieve of all the "relevant" sensor data and store it in a metrics database. 

The heatpump used for this experiment was a ground source heatpump, meaning that the source that the heatpump uses to extract heat from is relatively  constant. This is because ground sources lay deep in the ground, and are not affected by seasonal temperature changes like air heatpumps do. The brand of the heatpump is the Alpha Innotec.

## General setup  
The ground source heatpump at my home continuously measures data using its own sensors. Examples are metrics like outside temperature and total operational time of the heatpump. However is sensore data measured by the heatpump is not stored (it was not built that way), making it difficult to properly analyse it's behaviour. Therefore, I created a program which retrieves and stores sensor data from the heatpump each hour. 

The following diagram provides an overview of the components in my setup.

![diagram](diagram.png)

Each component is described shortly below:

* **Heatpump**. The Alpha Innotec heatpump of our house, the source my metrics.

* **Prometheus Exporter**. This represents to program I wrote. It retrieves sensor data from the heatpump and translates it to a format that is required by the Prometheus metrics database I used. To creae this program. first I needed to analyse the metrics that can be requested from the heatpump controller. From the heatpump manual I learned that it was using a Luxtronic controller board (a kind of mini computer) that I could use to retrieve metrics. The documentation for this controller board was quite scarce but fortunately I found a [web page](https://loxwiki.atlassian.net/wiki/spaces/LOX/pages/1533935933/Java+Webinterface) documenting the available metrics, making it easier to determine whicht variables/metrics could be useful.

* **Prometheus Metrics Database**. This is een open source database specially designed for storing metric data. It retrieves the sensor data form the prometheus exporter by calling the `/metrics` url of the program. In my case, a raspberry pi linux server was the host of the promotheus application, 24/7 active. The raspberry pi was used because it provides internet connection and enough storage for the prometheus application to run on. With this, the main program/ prometheus exporter program is also located on the raspberry. In short, the promtheus application is located in a raspberry pi, programmed to retrieve data from the prometheus exporter program each hour.

* **Grafana Dashboards**. This is also an open source solution for creating nice graphs/dashboards using the data inside the metrics database. In the example diagram below, you see a example what Grafana can creater without doing a lot of configuration. These diagrams are also automatically updated when new sensor data is stored in the prometheus metrics database.

![boiler hotwater temperature](graphs/boiler_hotwater_temperature.png)



## Raspberry Pi
All components except the heatpump itself are running on a tiny raspberry pi linux server put in the fusebox cupboard of the house. On this raspberry pi, the prometheus exporter program, the prometheus application and the grafana dashboard program. Meaning everything when logging in the raspberry pi through its own ip-adress. All the inforamtion is already to be displayed in graphs in matter of couple clicks.

-- TODO: insert photo here --


## metric configuration 
In the main program of the project, additional files were used because of the different reasons. One of these files contained the metrics used. Why? because it was easier to create/configure the metrics in another file than have the all metric configuration in the exporter program (main program). The latter could create a lot of errors and would not be easy to read and understand. 

The separate file for the metric configuration also allowed me to use another format than python. YAML was chosen because it is a configuration file format that can used with many different programming languages and is designed for human readability. I ended up with the following metric configuration file


https://github.com/m-swart/heatpump/blob/f0d0dfd7cc629cc823e801ce0b4e106fcd13a00b/metric.yml

As you can see, YAML made it very easy to define the metrics that the program needs to collect. Each invidual metric starts with the minus symbol `-`: 

```yaml
metrics:
  - name: heatpump_outdoor_temp_celcius
    key: ID_WEB_Temperatur_TA
    type: gauge
  - name: heatpump_operational_total_seconds
    key: ID_WEB_Zaehler_BetrZeitWP
    type: counter
```
As seen in the YAML file, each metrics consist out of a `name`, `key` and `type`. The `name` is just the name given to the metric to identify it. Looking at the example, from the name we can understand the metric is the outdoor temperature measured by the heatpump. 

The `key` is the essentially the name/key the program needs to use when asking the heatpump for data about the outdoor temperature. This is because the heatpump uses a programming language called Luxtronik, and otherwise the heatpump would not know what the program is asking for. 

The last element is the `type`, meaning the type of data. In the whole file, the only types are `guage` and `counter`. A guage is a value which can fluctuate over time, such as temperature. A counter is a value which can only increase. An example of a counter is time/age.
These types are important to display with the data, because otherwise prometheus does not understand how to store the data.


## Program explanation
> Please read metric configuration section first for better understanding.

I have written the Prometheus exporter program in Python. Main reason for using Python is that I was told it was easy to learn and that there already was a standard library available that would allow me to communicate with the heatpump controller.

https://github.com/m-swart/heatpump/blob/89292fa02aeb39303c1c5cff3516f7b67c08f38e/heatpump.py#L1-L3


The first three lines of code tell the program to install/import certain libraries so that the program understands what to do when referred to work with on the libraries further in the program.

A library is a addiotional file of code to be imported to your own code. This way the can reuse code written by others.

For this program, in total 3 librariers were installed and used using the pip3 python command. Library `Luxtronik` allows interaction with the heatpump controller and collect it's data. `Flask` is a web application framework for local/small usage. Flask can create a website on your own IP adress, which could serve as a place to display data. `Yaml` is a library that helps with reading configuration files in the [YAML](https://en.wikipedia.org/wiki/YAML) format.



Having installed the libraries needed for this project we start reading the YAML file containing the metrics the program has to collect from the heatpump.

https://github.com/m-swart/heatpump/blob/89292fa02aeb39303c1c5cff3516f7b67c08f38e/heatpump.py#L5-L7

Line 5 is a `#comment`, adding no meaning to the code. However in Line 6, the code tells te program to open a local file called metric.yml --> with permission `r`, implying that the program is only allow to read the file and not to modify it. 
Line 7 is a follow up to Line 6 telling the program to safeload/ preview and parse the data using the yaml library.

Everytime the program is to perform a new action, not a follow up to prior lines of code. A new "paragraph" (indentation) is used, so it is clear which paragraph does what.
https://github.com/m-swart/heatpump/blob/89292fa02aeb39303c1c5cff3516f7b67c08f38e/heatpump.py#L9

Line 9 is a function, defined by '='. It is a widely used function asking the program to create a Flask application using Flask. The code essentially tells the library to use library 'Flask' --> and current location of program '__name__' to create a 'app', or application.

The main and last part of the code is essentially a loop, to collect data of each metric listed in previously explained `metric.yml` file. 
https://github.com/m-swart/heatpump/blob/89292fa02aeb39303c1c5cff3516f7b67c08f38e/heatpump.py#L11-L22

Line 11 is the trigger for the loop L12-L22 to happen. Line 11 creates a specific URL/ app route so the application knows when to handle incoming web request. When that specific URL `/metrics` is requested Flask executes the function called `metrics`. The program ingnores Line 13 since it is a #comment. Line 14 asks the program to connect to a heatpump, using 'Luxtronik' and the local ip-adress to connect. 

Line 15 tells the program to prepare a response text for the metrics. ("") The response is still blank. So, Line 16 ask the program to get collect data for each individual metric in 'metrics.yml' from the heatpump. Lines 16 does this by creating a loop of L17-19. The program is able to identify each individual metric with the use of it's `-` prefix in the configuration file. Line 17 ask to program to find the value of that metric using the key of that metric. For example the value of key `ID_WEB_Temperatur_TA` using the Luxtronik library. Nothing is yet done with the response, is only stored in memory.

In Line 18, the program is asked to begin writing a response to be added in the blank space of line 15 ("") through 'metric_text +='. The program is asked to add  '# TYPE {0} {1}\n' to the reponse. {0} {1} are "strings". Whereas {0} represents the code 'metric['name']', and {1} represents 'metric['type']', both coming from the YAML file. The reason why {0} and {1} reperesent something is becasue of '.format' a rule in phyton creating these representations. The /n after {1} makes the program create a new line if something else would be added to the response later on.


Using the example above, response of Line 18 is this: 
```
#TYPE heatpump_outdoor_temp_celcius guage. 
```
Line 19 is about the same as Line 18. As explained earlier '+=' makes the program add the text/ reponse to 'metric_text'. However this time the program adds the name and the value of the metric to the response. The program gets the name of the metric from the YAML file and value was the response from the heatpump collected in Line 17. The value in Line 17 was earlier not added to reponses because no reponse space was given, and no add command was given. Which is '+='.

Using the example above, Line 19 would create this:
heatpump_outdoor_temp_celcius 8.9

The reason why the name and value have to be put in this specific order is because otherwise prometheus is not able to read/ take in the information. Promotheus is needed to fully automise this process of requesting the data and storing it.

Using the example above, the response from whole loop of L17-L19 creates this (example of 1 metric):
```
# TYPE heatpump_outdoor_temp_celcius gauge
heatpump_outdoor_temp_celcius 8.9
```

Line 20 tells the program to make `metric_text` the final response to the request. This response contains the work of L17-L19 of all the metrics in metric.yml because it is a loop of L16. Whereas this final response display is changed in Line 21. Although changing the format of the letters does not change anyhting to the program. When checking if the program was working, this format was easier to read.

Line 22 is the end of the loop. Where the program is told to send the final response to the computer requesting using Flask.




## Response
The program returns the following output in the format expected by Prometheus. See [documentation](https://prometheus.io/docs/instrumenting/exposition_formats/#text-format-example).

```
# TYPE heatpump_outdoor_temp_celcius gauge
heatpump_outdoor_temp_celcius 8.9
# TYPE heatpump_outdoor_temp_avg_celcius gauge
heatpump_outdoor_temp_avg_celcius 9.9
# TYPE heatpump_flow_in_temp_celcius gauge
heatpump_flow_in_temp_celcius 18.8
# TYPE heatpump_flow_out_temp_celcius gauge
heatpump_flow_out_temp_celcius 18.7
# TYPE heatpump_flow_out_target_temp_celcius gauge
heatpump_flow_out_target_temp_celcius 20.6
# TYPE heatpump_hotwater_measured_celsius gauge
heatpump_hotwater_measured_celsius 54.8
# TYPE heatpump_hotwater_target_celsius gauge
heatpump_hotwater_target_celsius 57.0
# TYPE heatpump_groundsource_in_temp_celsius gauge
heatpump_groundsource_in_temp_celsius 21.3
# TYPE heatpump_groundsource_out_temp_celsius gauge
heatpump_groundsource_out_temp_celsius 19.2
# TYPE heatpump_operational_total_seconds counter
heatpump_operational_total_seconds 42836049
# TYPE heatpump_operational_heating_seconds counter
heatpump_operational_heating_seconds 30253720
# TYPE heatpump_operational_hotwater_seconds counter
heatpump_operational_hotwater_seconds 12582318
# TYPE heatpump_operational_cooling_seconds counter
heatpump_operational_cooling_seconds 58770240
# TYPE heatpump_compressor_impulses counter
heatpump_compressor_impulses 37643
```


## Things I learned from this project
* Making simple programs in Python
* Working with GIT version control system
* Creating dashboards in Grafana
* Writing documentation in Markdown and publishing it on Github. 
* .......