#include <stdio.h>
#include <stdint.h>
#include <unistd.h>
#include "I2Cdev.h"
#include "MPU6050.h"

// class default I2C address is 0x68
// specific I2C addresses may be passed as a parameter here
// AD0 low = 0x68 (default for InvenSense evaluation board)
// AD0 high = 0x69
MPU6050 accelgyro;

int16_t ax, ay, az;
int16_t gx, gy, gz;

int axi = 0,ayi = 0,azi = 0,gxi = 0,gyi = 0,gzi = 0;

void setup() {
    // initialize device
    printf("Initializing I2C devices...\n");
    accelgyro.initialize();

    // verify connection
    printf("Testing device connections...\n");
    printf(accelgyro.testConnection() ? "MPU9150 connection successful\n" : "MPU9150 connection failed\n");
}

void loop() {
    // read raw accel/gyro measurements from device
    accelgyro.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);

    // these methods (and a few others) are also available
    //accelgyro.getAcceleration(&ax, &ay, &az);
    //accelgyro.getRotation(&gx, &gy, &gz);			
 
    static int count = 0;
		    
    if(count < 10) {
	axi += ax;
	ayi += ay;
	azi += az;
	gxi += gx;
	gyi += gy;
	gzi += gz;	

	++count;
	if(count == 10) {
		axi /= 10; ayi /= 10; azi /= 10;
		gxi /= 10; gyi /= 10; gzi /= 10;
	}

    } else {	 
			
    	// Refine Values
    	float f_ax = ((ax-axi) / ((float) (1 << 15)))*2.0;
    	float f_ay = ((ay-ayi) / ((float) (1 << 15)))*2.0;
    	float f_az = ((az-azi + (1<<14)) / ((float) (1 << 15)))*2.0;
	
    	float f_gx = ((gx-gxi) / ((float) (131)))*250.0;
    	float f_gy = ((gy-gyi) / ((float) (131)))*250.0;
    	float f_gz = ((gz-gzi) / ((float) (131)))*250.0;
	
	 // display accel/gyro x/y/z values
   	 printf("a/g: %.2f %.2f %.2f   %.2f %.2f %.2f\n",f_ax,f_ay,f_az,f_gx,f_gy,f_gz);
    }
}

int main()
{
    setup();
    printf("Initial configuration...\n");
    for (;;) {
        loop();
	usleep(100000);	
    }
}

