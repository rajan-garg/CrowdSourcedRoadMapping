import smbus
import time

bus=smbus.SMBus(1)
address=[0x1e,0x38,0x69,0x77]

def dataRead():
    for i in address[1:2]:
        print "Address: " + str(i)
        for j in range(0,24):
            print ("%5d"% (bus.read_byte_data(i,j))),
        print " "
        print " "
    print "="*210 

while True:
    newData=dataRead()
    time.sleep(3)
