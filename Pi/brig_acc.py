import smbus
import time

bus = smbus.SMBus(1)    # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)

DEVICE_ADDRESS = 0x38      #7 bit address (will be left shifted to add the read write bit)
DEVICE_REG_MODE1 = 0x00




#Write an array of registers
# ledout_values = [0xff, 0xff, 0xff, 0xff, 0xff, 0xff]
# bus.write_i2c_block_data(DEVICE_ADDRESS, DEVICE_REG_LEDOUT0, ledout_values)


##if doesn't work , possibly wrong function call write_byte_data may have to be changed with another
## function

def setupAcc():
	#bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_MODE1, 0x14)
	#initialConfig=bus.read_byte_data(DEVICE_ADDRESS,DEVICE_REG_MODE1)
        initialConfig=bus.read_byte_data(DEVICE_ADDRESS,0x14)
        
	##range has to be 10 or 01  test for 8g and 4g
	##bandwidth has to 100Hz 010
	##so total config is 10010
	##00000010
	#00000010

	##maintaining initial 3 bits
	initialConfig=initialConfig & (0xE0)
	##changing others
	initialConfig=initialConfig | (0x02)
	#bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_MODE1, 0x14)
	#bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_MODE1, initialConfig)
	bus.write_byte_data(DEVICE_ADDRESS, 0x14, initialConfig)

def getActual10bitData(data):
	##check whether negative or not?
	##we know data is first 10 bits only
	##for sanity check we can use bin function
	bits=10
	if(data&(1<<(bits-1)))!=0:
		data=data-(1<<bits)
	return data



def readAccData():
	# acc_x (02h, 7-6; 03h, 7-0)
	# acc_y (04h, 7-6; 05h, 7-0)
	# acc_z (06h, 7-6; 07h, 7-0)
	#bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_MODE1, 0x03)
	#data1=bus.read_byte_data(DEVICE_ADDRESS,DEVICE_REG_MODE1)
        ini_config=bus.read_byte_data(DEVICE_ADDRESS,0x15)
        ini_config=ini_config|0x08
        bus.write_byte_data(DEVICE_ADDRESS, 0x15,ini_config)
        
        data1=bus.read_byte_data(DEVICE_ADDRESS,0x03)
	#bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_MODE1, 0x02)
	#data2=bus.read_byte_data(DEVICE_ADDRESS,DEVICE_REG_MODE1)
        
	data2=bus.read_byte_data(DEVICE_ADDRESS,0x02)
	ini_config=ini_config&0xFB
	bus.write_byte_data(DEVICE_ADDRESS, 0x15,ini_config)
	#print "x-acc"+str(data1)
	#acc_x=((data1&(0xC0))<<2)|data2
	acc_x=(data1<<2)|(data2>>6)

	ini_config=bus.read_byte_data(DEVICE_ADDRESS,0x15)
        ini_config=ini_config|0x08
        bus.write_byte_data(DEVICE_ADDRESS, 0x15,ini_config)
        
        data1=bus.read_byte_data(DEVICE_ADDRESS,0x05)
	#bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_MODE1, 0x02)
	#data2=bus.read_byte_data(DEVICE_ADDRESS,DEVICE_REG_MODE1)
        
	data2=bus.read_byte_data(DEVICE_ADDRESS,0x04)
	ini_config=ini_config&0xFB
	bus.write_byte_data(DEVICE_ADDRESS, 0x15,ini_config)
	#print "x-acc"+str(data1)
	#acc_x=((data1&(0xC0))<<2)|data2
	acc_y=(data1<<2)|(data2>>6)

	ini_config=bus.read_byte_data(DEVICE_ADDRESS,0x15)
        ini_config=ini_config|0x08
        bus.write_byte_data(DEVICE_ADDRESS, 0x15,ini_config)
        
        data1=bus.read_byte_data(DEVICE_ADDRESS,0x07)
	#bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_MODE1, 0x02)
	#data2=bus.read_byte_data(DEVICE_ADDRESS,DEVICE_REG_MODE1)
        
	data2=bus.read_byte_data(DEVICE_ADDRESS,0x06)
	ini_config=ini_config&0xFB
	bus.write_byte_data(DEVICE_ADDRESS, 0x15,ini_config)
	#print "x-acc"+str(data1)
	#acc_x=((data1&(0xC0))<<2)|data2
	acc_z=(data1<<2)|(data2>>6)

	#bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_MODE1, 0x05)
	#data1=bus.read_byte_data(DEVICE_ADDRESS,DEVICE_REG_MODE1)
	#bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_MODE1, 0x04)
	#data2=bus.read_byte_data(DEVICE_ADDRESS,DEVICE_REG_MODE1)
	#print "y-acc"+str(data1)
	#acc_y=((data2&(0xA0))<<2)|data1
	#bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_MODE1, 0x07)
	#data1=bus.read_byte_data(DEVICE_ADDRESS,DEVICE_REG_MODE1)
	#bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_MODE1, 0x06)
	#data2=bus.read_byte_data(DEVICE_ADDRESS,DEVICE_REG_MODE1)
	#print "z-acc"+str(data1)
	#acc_z=((data2&(0xA0))<<2)|data1

	##convert data into appropriate positive or negative values
	acc_x=getActual10bitData(acc_x)
	acc_y=getActual10bitData(acc_y)
	acc_z=getActual10bitData(acc_z)

	acc_data=[]
	acc_data.append(acc_x)
	acc_data.append(acc_y)
	acc_data.append(acc_z)
	return acc_data





##main code

setupAcc()
while True:
	acc_data=readAccData()
	time.sleep(1)
	print "x: %d y: %d z; %d "%(acc_data[0],acc_data[1],acc_data[2])
	#print "%d %d %d"% (acc_data[0]),acc_data[1],acc_data[2])
