import paho.mqtt.client as mqtt

mqttc = mqtt.Client("python_pub")
mqttc.connect("0.0.0.0", 1883)
bumpData=open("bump_merge.txt","r");
mqttc.publish("helloworld", "hello",0,False)
bumpData.close()
mqttc.loop(2) 
