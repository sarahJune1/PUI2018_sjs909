#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 16:04:25 2018

@author: SarahJune
"""
from __future__ import print_function
import json
import os
# the next import allows me to read line input arguments
import sys

try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

apikey = sys.argv[1]
BUS_LINE = sys.argv[2]

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(apikey,BUS_LINE)

if not len(sys.argv) == 4:
    print ("Invalid number of arguments. Run as: python get_bus_info_sjs909.py xxxx-xxxx-xxxx-xxxx-xxxx <BUS_LINE> <BUS_LINE>.csv")
    sys.exit()
    
print(url)
response = urllib.urlopen(url)
MTAdata = response.read().decode("utf-8")
#use the json.loads method to obtain a dictionary representation of the responose string 
MTAdata = json.loads(MTAdata)

# open a file for writing using name you chose
fout = open(sys.argv[3], "w")
busNum = len(MTAdata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])

for i in range(busNum):
    try:
        Stop_Status = MTAdata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
        Stop_Name = MTAdata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][1]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][i]['StopPointName']
        lat = MTAdata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
        long = MTAdata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    except KeyError:       
        Stop_Status ='N/a'
        Stop_Name = 'N/a'
   
    print(str(lat) + str(long) + str(Stop_Name)+ " is " + str(Stop_Status))
    fout.write(str(lat)+ ',' + str(long)+ ','+str(Stop_Name)+ ','+str(Stop_Status)+"\n")