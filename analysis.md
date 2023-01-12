# Energy comsumption of a heatpump during the winter
In this small report, the data collected from the heatpump will be anaysed and evaluated. The goal of the report is inform readers whom may be considering to get a heatpump as an alternative heatpump. In the report, energy usage of the heatpump will be discussed and how much the cost can be when running the heatpump daily. Furthermore an explanation why an heatpump can use high amounts of energy during the winter.

### Validity of the analysis
All the graphs of information used for this analysis comes from one singular heatpump. Therefore the validaty of the anaylsis can be questioned. However just recent, the heatpump had control, and came through with no mechanical problems. The type of heatpump used for this project provides heating for a family of 4, is a ground-source heatpump and uses 2.6 kwh to heat 207m squared of housing, however can the analysis of the data collected be useful for everybody. Why? this is because this winter had a diversification of temperatures providing a lot of instresing trends in correlation between outside temperature and operational hours of the heatpump.

### Operational hours of the heatpump
![boiler hotwater temperature](graphs/Heatpump_hotwater_operational_hours_per_day_90days.png)
Graph 1 - heatpump operational hours per day

Graph 1 shows the operational hours per day of the heatpump since around 11/01/22. In the graph, the yellow part of the bar represents the hours the heatpump has been heating the house, and the green part represents the time the heatpump has been heating the tapwater of our house. Based from graph 1, heating of tapwater was often constant around 1 hour. Between 12/16 and 12/20 more heating for tapwater was needed. During this period, another family of 4 was present in the house. Indicating the use of warm tapwater equals time the heatpumps needs to operate to some extend.

![boiler hotwater temperature](graphs/boiler_hotwater_temperature_.png)
Graph 2 - the temperature of the water heater barrel

The reason why the heatpump always needs to operate although no warm water is used in the house. As shown in the graph, the temperature of the water heater barrel, or the temperature of the barrel holding the warm tapwater is constantly dropping in temperature and is heated constantly back to 56 celcius. This is caused by the barrel not being perfectly isolated, meaning the heatpump constantly needs to add heat/ energy to the barrel.

![boiler hotwater temperature](graphs/Heatpump_hotwater_operational_hours_per_day_90days.png)
Graph 1 - heatpump operational hours per day

As seen in Graph 1, the yellow part of the bar graph/ the time heating the house is the opposite of heating the tapwater, it is not controlled. To explore why it is in that way, we must look at the outside temperature.

![boiler hotwater temperature](graphs/outside_temperature_90days.png)
Graph 3 - outside temperature for the last 90days

NOTE: the reason why data is missing is because the raspberry pi crashed and was not much noticed later, but the single trend on the left of graph 3 serves useful.

When comparing graph 1 and 3, there is a clear relation between outside temperature and time the heatpump is heating the house (note heatpump heating the house is constant). The relation between the graphs is that when temperatures tend to be low, the operational hours of the heatpump heating the home is high. This especially can be seen at 12/18 when outside temperatures reached -8 degrees and the heatpump spend a total of 7/8 hours heating the home. Opposite can be seen early November, when temperatures were high and heating of the house was no more than 2 hours. This can be explained scientifically since heat temperature always tries to move to low temperatures and equalize "presure" (“Heat Transfer”). The reason why the cold weather does not affect the cooling down of the barrrel with tapwater is because the barrel is placed underground level, better isolated, and is exposed to room temperature and not exposed to direct cold air like an house. Furthermore is it a loss less efficient to heat up bigger environments, resulting in longer heating hours.

Sometimes the heatpump does not heat the house at all, the explantion behind that is when it is warm and sunny, the house can be heated using the solar collectors our house on the roof. However was this not counted in the investigation, between during the winter (time of collecting data), the solar collectors are most of time off from activity.

![boiler hotwater temperature](graphs/heating_kwh_estimate_per_day_90days.png)


how the heatpumps works


