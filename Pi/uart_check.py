#!/usr/bin/python
from serial import Serial
 
#Starting serial connection
serialPort = Serial("/dev/ttyAMA0", 9600, timeout=1)
#Check if port failed to open
if (serialPort.isOpen() == False):
        serialPort.open()
 
#Flush before receiving or sending any data
serialPort.flushInput()
serialPort.flushOutput()
 
#String as output
serialPort.write('scaluza.com')
while True:
        #Check if there is any byte waiting on serial port
        if(serialPort.inWaiting() != 0):
                #Read 1 byte at a time
                input = serialPort.read(1)
                print input
 
#Closing serial port
serialPort.close()
