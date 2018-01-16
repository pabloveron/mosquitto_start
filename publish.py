# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
import sys

mqttc = mqtt.Client("python_pub")
mqttc.connect("172.17.0.3", 1883)
mqttc.publish("broker/messages", sys.argv[1])
mqttc.loop(2) #timeout = 2s
