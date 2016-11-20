import math,time

def toDegrees(l):
	l = float(l) 
	t = int(l/100)*100
	m = (l - t)/60
	return (t/100) + m

def toVal(acc):
	r,am = 0,0
	acc = int(acc)
	if abs(acc-am) > 2200:
		r = 2
	elif abs(acc-am) > 1500:
		r = 1
	return 2*r+1

t = 0
while True:
	# with open("wifi_raw.txt") as f:
	# 	lines = f.readlines()

	# data = 'setInterval(function() {console.log("Plotting new."); if(typeof heatmap !== "undefined") {heatmap.setMap(null);} eqfeed_callback({"type":"FeatureCollection","features":['
	# for idx, line in enumerate(lines):
	# 	if line == "x\n" or line == "\n" or line == "":
	# 		continue
	# 	lat,lng,mag,tilt,acc = line.split(',')
	# 	# mag,lat,lng = line.split(',')
	# 	mag = float(mag)*10
	# 	lat = toDegrees(lat)
	# 	lng = toDegrees(lng)
	# 	data += '{"type":"Feature","properties":{"mag":' + str(mag) + '},"geometry":{"type":"Point","coordinates":[' + str(lat) + "," + str(lng) + ']}}'
	# 	if idx != len(lines)-1:
	# 		data += ',' 
	# data += ']});},15000);'

	# f = open('wifi.js','w')
	# f.write(data)
	# f.close()

	with open("wifi_raw.txt") as f:
		lines = f.readlines()

	data = 'eqfeed_callback({"type":"FeatureCollection","features":['
	for idx, line in enumerate(lines):
		if line == "x\n" or line == "\n" or line == "":
			continue
		# lat,lng,mag,tilt,acc = line.split(',')
		mag,lat,lng = line.split(',')
		mag = float(mag)*10
		lat = toDegrees(lat)
		lng = toDegrees(lng)
		data += '{"type":"Feature","properties":{"mag":' + str(mag) + '},"geometry":{"type":"Point","coordinates":[' + str(lat) + "," + str(lng) + ']}}'
		if idx != len(lines)-1:
			data += ',' 
	data += ']});'

	f = open('wifi.js','w')
	f.write(data)
	f.close()

# with open("bump_merge.txt") as f:
# 	lines = f.readlines()
# data = 'bumps = ['
# for idx, line in enumerate(lines):
# 	lat,lng = line.split(',')
# 	lat = toDegrees(lat)
# 	lng = toDegrees(lng)
# 	data += '[' + str(lat) + "," + str(lng) + ']'
# 	if idx != len(lines)-1:
# 		data += ','
# data += '];'

# f = open('bumps.js','w')
# f.write(data)
# f.close()

# with open("tilt_merge.txt") as f:
# 	lines = f.readlines()
# data = 'tilts = ['
# for idx, line in enumerate(lines):
# 	lat,lng = line.split(',')
# 	lat = toDegrees(lat)
# 	lng = toDegrees(lng)
# 	data += '[' + str(lat) + "," + str(lng) + ']'
# 	if idx != len(lines)-1:
# 		data += ','
# data += '];'

# f = open('tilts.js','w')
# f.write(data)
# f.close()

# with open("final_acc_merge.txt") as f:
# 	lines = f.readlines()
# data = 'var roadPlanCoordinates = ['
# for idx, line in enumerate(lines):
# 	lat,lng,mag = line.split(',')
# 	lat = toDegrees(lat)
# 	lng = toDegrees(lng)
# 	data += '{lat:' + str(lat) + ",lng:" + str(lng) + '}'
# 	if idx != len(lines)-1:
# 		data += ','
# data += '];'

# f = open('road.js','w')
# f.write(data)
# f.close()

	# with open("road_data.txt") as f:
	# 	lines = f.readlines()
	# data = 'setInterval(function() {console.log("Plotting new."); if(typeof heatmap !== "undefined") {heatmap.setMap(null);}  terrainCallback(['
	# for idx, line in enumerate(lines):
	# 	if line == "x\n" or line == "\n" or line == "":
	# 		continue
	# 	lat,lng,mag,tilt,acc = line.split(',')
	# 	lat = toDegrees(lat)
	# 	lng = toDegrees(lng)
	# 	acc = toVal(acc)
	# 	data += '{location: new google.maps.LatLng(' + str(lat) + "," + str(lng) + '), weight:' + str(mag) + '}'
	# 	if idx != len(lines)-1:
	# 		data += ','
	# data += ']);}, 15000);'

	# f = open('terrain1.js','w')
	# f.write(data)
	# f.close()


	time.sleep(3)

