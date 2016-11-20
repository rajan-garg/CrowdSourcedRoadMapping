import os,time

while True:
	outputLines=os.popen("sudo iwlist wlan0 scan | grep -e 'ESSID' -e 'Quality'").readlines();
	signals={}
	i=0
	while i<len(outputLines):
		quality=outputLines[i].split("=")[1].split(" ")[0].split("/")
		quality_ratio=float(quality[0])/float(quality[1])
		essid=outputLines[i+1].split(":")[1].strip()
		if essid in signals:
			if signals[essid]<quality_ratio:
				signals[essid]=quality_ratio	
		else:
			signals[essid]=quality_ratio
		#print quality_ratio,essid,
		i+=2

	millis = int(round(time.time() * 1000))//1000
	print str(millis) + " ",
	for key in signals:
		print key + " " + str(signals[key]) + " ",
	print

