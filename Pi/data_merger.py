import itertools
import time
import paho.mqtt.client as mqtt

time.sleep(10)

mqttc = mqtt.Client("python_pub")
mqttc.connect("0.0.0.0", 1883)


def getTimeOfgpsLine(line):
	return long(line.split(',')[0].strip())
def getTimeOfWifiLine(line):
	return long(line.split(' ')[0].strip())
def getTimeOfAccLine(line):
	return long(line.split(' ')[0].strip())
def getIITGwifiStrength(line):
	wifiList=(line.split(' '))	
	iitgFound=False
	for wifi in wifiList:
		if iitgFound:
			return float(wifi.strip())
		if 'IITG_WIFI' in wifi:
			iitgFound=True
	return None
def getLatLong(line):
	data=line.split(',')
	if (data[1]==''):
		return None
	return (float(data[1]),float(data[2].strip()))
	
	

gpsData=open('gps.txt','r')
wifiData=open('wifi.txt','r')
accData=open('/home/pi/PiBits/MPU6050-Pi-Demo/acc_data.txt','r')
accLine=accData.next()
mergedData=open('merge.txt','a+')
accHigh=False
gpsHigh=False
wifiHigh=False
gpsLine=""
wifiLine=""
gpsTime=0
wifiTime=0
accTime=0
oldTime=int(round(time.time() * 1000))//1000
diff=0
sendCnt=0
data=""
#try:
if True:
	while True:
		if sendCnt==10:
			mqttc.publish("helloworld",data,0,False)
			mqttc.loop(2)
			print "should"
			data=""
			sendCnt=0
		sendCnt+=1
		
		diff=0
		while diff<1:
			newTime=int(round(time.time() * 1000))//1000
			diff=newTime-oldTime
			#print diff
		#print "iteration"
		oldTime=newTime	
		if not gpsHigh:
			gpsLine=gpsData.next()
			gpsTime=getTimeOfgpsLine(gpsLine)
		if not wifiHigh:
			wifiLine=wifiData.next()
			wifiTime=getTimeOfWifiLine(wifiLine)
		if not accHigh:
			accLine=accData.next()
			accTime=getTimeOfAccLine(accLine)
		if gpsTime>wifiTime:
			gpsHigh=True
			wifiHigh=False
			if accTime<gpsTime:
				accHigh=False
			elif accTime>gpsTime:
				gpsHigh=False
				accHigh=True
			else:
				accHigh=False
		elif gpsTime<wifiTime:
			gpsHigh=False
			wifiHigh=True
			if accTime<wifiTime:
				accHigh=False
			elif accTime>wifiTime:
				wifiHigh=False
				accHigh=True
			else:
				accHigh=True
		elif accTime<gpsTime:
			accHigh=False
			gpsHigh=True
			wifiHigh=True
		elif accTime>gpsTime:
			accHigh=True
			gpsHigh=False
			wifiHigh=False
		else:
			gpsHigh=False
			wifiHigh=False
			accHigh=False
			wifiStrength=getIITGwifiStrength(wifiLine)
			if wifiStrength is None:
				#print "wifi wrong"
				#continue
				pass
			latLong=getLatLong(gpsLine)
			
			if latLong is None:
				#print "gps wrong"
				data+="x\n"
				#mqttc.publish("helloworld","hello uppinder",0,False)
				#mqttc.loop(10)
				continue
				#pass
			accList=accLine.split(' ')
			#print accList
			if wifiStrength is None:
				#mergedData.write("%s,%s,%s,%s,%s\n"%(str(latLong[0]),str(latLong[1]),str(wifiStrength),accList[1],accList[2]))
				#print  "%s,%s,%s,,%s\n"%(str(latLong[0]),str(latLong[1]),accList[1],accList[2])
				data+="%s,%s,0,%s,%s\n"%(str(latLong[0]),str(latLong[1]),accList[1],accList[2])
				
				#data+="%s,%s\n"%(accList[1],accList[2])
			else:
				#print "%s,%s,%s,%s,%s\n"%(str(latLong[0]),str(latLong[1]),str(wifiStrength),accList[1],accList[2])
				data+="%s,%s,%s,%s,%s\n"%(str(latLong[0]),str(latLong[1]),str(wifiStrength),accList[1],accList[2])
			
				#data+="%s,%s,%s\n"%(str(wifiStrength),accList[1],accList[2])
			#mqttc.loop(2)
			
if True:	
#except:
	gpsData.close()
	wifiData.close()
	mergedData.close()
	
		
#with open('gps.txt') as bf1:
#    with open('gps') as bf2:
#        for line1, line2 in itertools.izip(bf1, bf2):
#            process(line1, line2)
