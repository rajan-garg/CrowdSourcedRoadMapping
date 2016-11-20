import os,csv

with open("acc_data.txt") as f:
	content = f.readlines()

data = []
for c in content:
	c = c[:-1]
	data.append(c.rstrip().split(" "))

data = data[1:]
#print data

length = len(data)

with open("data.csv","wb") as file:
	file_writer = csv.writer(file)
	for i in range(length):
		file_writer.writerow(data[i])
