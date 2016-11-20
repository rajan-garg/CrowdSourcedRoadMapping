import paho.mqtt.client as mqtt
message = 'ON'
file=open("road_data.txt","w")

def on_connect(mosq, obj, rc):
    mqttc.subscribe("helloworld", 0)
    print("rc: " + str(rc))

def on_message(mosq, obj, msg):
    global message
    file.write(str(msg.payload))
    file.flush()
    print(str(msg.payload))
    message = msg.payload
    #mqttc.publish("f2",msg.payload);

def on_publish(mosq, obj, mid):
    print("mid: " + str(mid))

def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(mosq, obj, level, string):
    print(string)


mqttc = mqtt.Client()
# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
# Connect
mqttc.connect("192.168.43.128", 1883,60)


# Continue the network loop
mqttc.loop_forever()