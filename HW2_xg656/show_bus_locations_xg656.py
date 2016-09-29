from __future__ import print_function
import json
import urllib2
import os
import sys
import numpy as np



apikey=sys.argv[1]
busline=sys.argv[2]

url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&Ve"+\
"hicleMonitoringDetailLevel=calls&LineRef=%s'%(apikey,busline)

response = urllib2.urlopen(url)
data = response.read().decode("utf-8")

#use the json.loads method to obtain a dictionary representation of the responose string 
dataDict = json.loads(data)
#print (dataDict)
#type(dataDict)
location=dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][1]['MonitoredVehicleJourney']['VehicleLocation']
busnum = np.size(dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])
location_part1=dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

print("Bus Line : "+str(busline))
print("Number of Active Buses : "+str(busnum))
for i in range(0,int(busnum)):
    Latitude=str(location_part1[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])
    Longtitude=str(location_part1[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])
    print("Bus "+str(i)+" is at latitude "+Latitude+" and longitude "+Longtitude)
#############Begin of Output format:
#Bus Line : B52
#Number of Active Buses : 5
#Bus 0 is at latitude 40.687241 and longitude -73.941661
#############End of Output format
