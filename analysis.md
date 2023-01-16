# Energy comsumption of a heatpump during the winter
In this small report, the data collected from the heatpump will be analysed and evaluated. The goal of the report is to inform readers whom may be considering to get a heatpump as an alternative heating source. In the report, energy usage of the heatpump will be discussed and I'll try to provide an indication of the cost of running a heatpump as the sole energy source for both heating an hot water supply. 

### Validity of the analysis
The heatpump used for my observations recently had a technical check and came through without problems. The type of heatpump used for this project provides heating for a relatively modern and well isolated house of approximately 207sqm. The house is used by a family of 4.
The heatpump is a ground-source heatpump and uses according to vendor specifications on average 2.6 kwH. 
All the data used for this analysis come from one single heatpump. In other words we have a sample of 1 (n=1). Therefore, we cannot generalize the conclusions to be valid for all houses with heatpumps. Nevertheless, I do think it can give proper insights for people that are considering to install a heatpump for they own house. The measurements were made during a winter period and had a diverse temperatures providing a lot of insteresting trends illustrating a relationship between outside temperature and operational hours of the heatpump.

### Operational hours of the heatpump
![boiler hotwater temperature](graphs/Heatpump_hotwater_operational_hours_per_day_90days.png)
**_Graph 1 - heatpump operational hours per day_**

Graph 1 shows the operational hours per day of the heatpump since the start of November 2022. The heatpump used in my analysis as to major roles:

1. **Heating**. The heatpump has to heat the house. The time it spend on this is provided by the yellow part of the bar.
2. **Hot water**. The heatpump is also responsible for hot water supply (inside a hot water tank). The time spend on ensuring enough hot water is provided by the green part of the bar. 

The heatpump can only execute one task at a time. So it is either heating the house, heating tap water or doing nothing. 

Based from graph 1, heating of tapwater was averaging just below 1 hour per day. Between 12/16 and 12/20 more heating for tapwater was needed. During this period, another family of 4 was also staying in the house resulting in a significantly higher time spend on heating water. This suggest a clear (and to be expected) relationship between the consumption of warm tapwater and the time the heatpump spend on heating tap water. 

![boiler hotwater temperature](graphs/boiler_hotwater_temperature_.png)
**_Graph 2 - the temperature of the hot water tank_**

The heatpump sometimes also needs to operate in periods where no warm water is used in the house, for example during the night. As shown in the graph, the temperature of the water heater barrel, or the temperature of the barrel holding the warm tapwater is constantly dropping in temperature and is heated constantly back to 56 celcius. This is caused by the barrel not being perfectly isolated, meaning the heatpump constantly needs to add heat/energy to the barrel.

As can be seen in Graph 1, the time spend on heating the house (the yellow part of the bar graph) varies much more that the time spend on  heating the tapwater. To explore why it is in that way, we must look at the outside temperature.

![boiler hotwater temperature](graphs/outside_temperature_90days.png)
**_Graph 3 - outside temperature for the last 90days_**

> NOTE: the reason why data is missing is because the raspberry pi crashed due to a power outage and did not properly restart. Unfortunately this was only noticed more that a week later. Nevertheless, the general trend of the graph is still useful.

When comparing graph 1 and 3, there is a clear relation between outside temperature and time the heatpump spends on heating the house. The relation between the graphs is that when temperatures tend to be low, the operational hours the heatpump spends on heating is high. This especially can be seen at 12/18 when outside temperatures reached -8 degrees and the heatpump spend a total of 7 to 8 hours heating the home. The opposite can be seen early November, when temperatures were high and heating of the house took no more than 2 hours and on some days even 0 hours. This phenomenon we all intuitively "know" is defined in the second law of thermodynamics says that heat flows naturally from an object at a higher temperature to an object at a lower temperature. It does not flow in the opposite direction of its own accord.

The reason why the cold weather does not affect the cooling down of the barrrel with tapwater is because the barrel is placed underground level, better isolated, and is exposed to room temperature and not exposed to direct cold air like the rest of the house.

On some some days the heatpump does not need to spend time on hot water at all, This is because when it is warm and sunny, the hot water tank can be heated using the solar collectors on the roof of the house. However, this does not happen frequently during the winter period.

## The cost of running a heatpump
![boiler hotwater temperature](graphs/heating_kwh_estimate_per_day_90days.png)
**_Graph 4 - usage kWh per day of heatpump_**

Some heatpumps can use a lot of energy. The one used for the experiment uses in average 2.6 kWh. Which can be quite a lot, since it can have a operational time of 10 hours during cold winters. This can be quite costly considering the prices in Europe have increased significantly over the last year. 

For example the average kWh use of the heatpump per day this warm winter was around 5 KWh. Taking the current electricty prices of €90c/kWh this amounds to just under €5 euros per day or €135 euros per month just soley to power the heatpump. Still, when compared to gas furnaces, it is relatively cheap.

A major disadvantage of a heatpump is that it is an expensive piece of machinery. Especially if you include installation cost and drilling of the ground-source. Addionally you need a very good isolated house, preferably with full floor heating. This makes heatpumps unfortunately not the best option for everyone. 

An important advantage of the heatpump that it solely relies on electricity which potentially can be sourced from renewable sources. A heatpump only uses electricity because the heatpump is able to compress matter of low temperature into higher temperatures. Which the matter is often a liquid or air coming from the outside. This compress mechanism is performed by a compressor (of gas), which is the main energy consumer when heating your home (“Hoe Werkt Een Warmtepomp?”). This makes the heatpump a very reliable and independent source of energy. Which is very sustainable (because most energy/ heat comes from the outside) and can be handy in times of war, such as now, whereas gas prices are higher than electricity.

## Conclusion
Although not a lot of arguments were reviewed in this report. From the information covered can a heatpump be very useful for a lot of households, esecially sinds it is a very sustainable and indepdent source of heat. However can the prices of installing and running a heatpump skyrocket, and is often only beneficial in the long-term over 10 years. Especially in the current situation, a heatpump is for many households not the best option and is it the best to look for something else. However for the people whom have additional money saved, installing a heatpump over the long-term will be worth it.
