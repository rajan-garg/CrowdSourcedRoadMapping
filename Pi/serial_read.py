import time
import serial


ser = serial.Serial(

		port='/dev/ttyAMA0',
		baudrate = 9600,
		parity=serial.PARITY_NONE,
		stopbits=serial.STOPBITS_ONE,
		bytesize=serial.EIGHTBITS,
		timeout=1
		)
counter=0

f1 = open("gps_data.txt", "a+");
f1.write("--------------------------------------------------");

i = 600
while i > 0:
	x=ser.readline()
	f1.write(x + "\n")
	i -= 1

f1.close()

