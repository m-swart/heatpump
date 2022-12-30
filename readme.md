# Milans personal project


## Introduction
Write about personal project, goals etc:

This repository contains my work done for my personal project. 


### Learning goal


### Product goal


## Heatpumps




## General setup  
The following diagram provides an overview of the components in my setup.

![diagram](diagram.png)


### Heatpump
Alpha Innotec heatpump

### Prometheus Exporter


### Prometheus Metrics Database


### Grafana Dashboards




All components except the heatpump itself are running on a tiny raspberry pi linux server in our 'meterkast'.

-- insert photo here --


## The heatpump data exporter
In order to get the heatpump metrics in the Prometheus metrics database I had to write a so called prometheus exporter program. This program convert the heatpump metrics into a format that Prometheus understands.

First I needed to analyse the metrics that can be requested from the heatpump controller. From the heatpump manual I learned that it was using a Luxtronic controller board (a kind of mini computer) that I could use to retrieve metrics. The documentation for this controller board was quite scarce but fortunately I found a web page documenting the available metrics.





### program outline
I have written the Prometheus exporter program in Python. Main reason for using Python is that I was told it was easy to learn and that there already was a standard library available to allowed me to communicate with the heatpump controller.

https://github.com/m-swart/heatpump/blob/89292fa02aeb39303c1c5cff3516f7b67c08f38e/heatpump.py#L1-L3


The first three lines of code tell the program to install/ import certain libraries. So that the program understands what to do when referred to work with on the libraries further on. A library is a addiotional file of code to be imported to your own code. Benefits of this are that existing code can be reused.

For this program, in total 3 librariers were (pip3) installed and used. Library Luxtronik allows interaction between the heatpump controller, essential to collect data. Flask is a web application framework for local/ small uses, fask can create a website on your own IP adress, which could serve as a place to display data. Yaml is a library that helps with reading configuration files in the [YAML](https://en.wikipedia.org/wiki/YAML) format.




 Which can consist out of 
widely 



## Grafana dashboard




## Things I learned

* Making simple programs in Python
* Working with GIT version control system
* Creating dashboards in Grafana
* Writing documentation in Markdown and publishing it on Github. 
* .......