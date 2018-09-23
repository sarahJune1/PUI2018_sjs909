#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 13:53:14 2018

@author: SarahJune
"""

from __future__ import print_function
import json
import os
# read line input arguments
import sys
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

apikey = sys.argv[1]
BUS_LINE = sys.argv[2]

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(apikey,BUS_LINE)

if not len(sys.argv) ==3:
    print("Invalid number of arguments. Run as: python  show_bus_locations_sjs909.py <MTA_KEY> <BUS_LINE>")
    sys.exit()
    

print(url)
response = urllib.urlopen(url)
MTAdata = response.read().decode("utf-8")
#use the json.loads method to obtain a dictionary representation of the responose string 
MTAdata = json.loads(MTAdata)


print("Bus Line : " + BUS_LINE)
#print("Number of Active Buses : " + DistanceFromCall)
print("Number of Active Buses : ")
print(len(MTAdata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']))
print("Bus 0 is at: " )
print(MTAdata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][0]['MonitoredVehicleJourney']['VehicleLocation'])
print("Bus 1 is at: " )
print(MTAdata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][1]['MonitoredVehicleJourney']['VehicleLocation'])
print("Bus 2 is at: " )
print(MTAdata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][2]['MonitoredVehicleJourney']['VehicleLocation'])
print("Bus 3 is at: " )
print(MTAdata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][3]['MonitoredVehicleJourney']['VehicleLocation'])
print("Bus 4 is at: " )
print(MTAdata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][4]['MonitoredVehicleJourney']['VehicleLocation'])
print("Bus 5 is at: " )
print(MTAdata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][5]['MonitoredVehicleJourney']['VehicleLocation'])
print("Bus 6 is at: " )
print(MTAdata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][6]['MonitoredVehicleJourney']['VehicleLocation'])
print("Bus 7 is at: " )
print(MTAdata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][7]['MonitoredVehicleJourney']['VehicleLocation'])

