from __future__ import print_function
import json
import urllib2
import os
import sys
import numpy as np
import pandas as pd


apikey=sys.argv[1]
busline=sys.argv[2]
filename=sys.argv[3]

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

Distance=location_part1[0]['MonitoredVehicleJourney']['MonitoredCall']['Extensions']['Distances']['PresentableDistance']
df=pd.DataFrame(dataDict,columns=['Latitude','Longitude','Stop Name','Stop Status'])

temp1= pd.DataFrame(columns=['Latitude','Longitude','Stop Name','Stop Status'])
for i in range(0,int(busnum)):
    Latitude=str(location_part1[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])
    Longtitude=location_part1[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    temp=location_part1[i]['MonitoredVehicleJourney']['OnwardCalls']
    if ('OnwardCall' in temp)==0:
        Stop='N/A'
        Distance='N/A'
    else:
        Stop=location_part1[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
        Distance=location_part1[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
    temp2=pd.DataFrame({'Latitude':[Latitude], 'Longitude':Longtitude, 'Stop Name':Stop, 'Stop Status':Distance})
    temp1=temp1.append(temp2)
df=temp1
df.to_csv(filename, index=0)
#############Begin of Output format:
#Latitude,Longitude,Stop Name,Stop Status
#40.755489,-73.987347,7 AV/W 41 ST,at stop
#40.775657,-73.982036,BROADWAY/W 69 ST,approaching
#40.808332,-73.944979,MALCOLM X BL/W 127 ST,approaching
#40.764998,-73.980416,N/A,N/A
#40.804702,-73.947620,MALCOLM X BL/W 122 ST,< 1 stop away
#40.776950,-73.981983,AMSTERDAM AV/W 72 ST,< 1 stop away
#40.737650,-73.996626,AV OF THE AMERICAS/W 18 ST,< 1 stop away
#############End of Output format
