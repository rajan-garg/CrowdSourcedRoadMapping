#!/usr/bin/python

import os
try:
	#os.remove('/home/pi/PiBits/MPU6050-Pi-Demo/acc_data.txt')
	#os.remove('/home/pi/gps.txt')
	pass
except:
	pass
from serial import Serial
from pynmea import nmea
import time
#Starting serial connection
serialPort = Serial("/dev/ttyAMA0", 9600, timeout=1)
#Check if port failed to open
if (serialPort.isOpen() == False):
        serialPort.open()

#Flush before receiving or sending any data
serialPort.flushInput()
serialPort.flushOutput()

#String as output
#serialPort.write('scaluza.com')
gpsData=""
gpgga = nmea.GPGGA()
f1=open('gps.txt','w+')
while True:
	
        #Check if there is any byte waiting on serial port
        if(serialPort.inWaiting() != 0):
                #Read 1 byte at a time
                input = serialPort.read(1)
                #print input.decode('utf-8')
		if input=='\n':
			if gpsData[0:6]=='$GPGGA':
				gpgga.parse(gpsData)
				#print gpgga
				millis = int(round(time.time() * 1000))//1000		
				#f1.write("%s,"%str(millis))		
				lats = gpgga.latitude
				longitude = gpgga.longitude
				#f1.write(str(millis)+","+str(lats)+","+str(longitude)+"\n")
				print str(millis)+","+str(lats)+","+str(longitude)
				#lat_dir = gpgga.lat_direction
				#print "Latitude direction : " + str(lat_dir)
				#time_stamp = gpgga.timestamp
				#print "GPS time stamp : " + str(time_stamp)
			gpsData=""
		else:
			gpsData+=input
#Closing serial port
serialPort.close()

