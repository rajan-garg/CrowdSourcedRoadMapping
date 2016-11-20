#!/bin/bash

#sleep 60

sudo python -u /home/pi/get_wifi_data.py > /home/pi/wifi.txt &
sudo python -u /home/pi/get_gps_data.py > /home/pi/gps.txt &
/home/pi/PiBits/MPU6050-Pi-Demo/demo_dmp &
cd /home/pi
python data_merger.py
