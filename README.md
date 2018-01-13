# mosquitto and raspbian likte
Simple mosquitto project to subscribe and publish messages running in raspberry py from scratch

## Steps to install mosquitto from scratch (on RASPBIAN STRETCH LITE)

- Update the package update list. Download the list to keep the versions updated.
	- sudo apt-get update

- Dist upgrade sudo. Will install the packages to resolve the dependencies
	- apt-get dist-upgrade

- Install mosquitto and mosquitto-clients that includes command clients applications to test publisher and subscriber features
	- sudo apt-get install mosquitto mosquitto-clients -y
	
- Enable the subscriber test client
	- mosquitto_sub -t “testqueue/testtopic”

- Send the message using publisher client
	- mosquitto_pub -t “testqueue/testtopic” -m “testing”

### Python code to publish and subscribe

First of all, need to install python tools and library paho-mqtt
	- sudo apt-get install python-pip
	- pip install paho-mqtt


Here the inspiration source code [link1](www.eclipse.org/paho/clients/python/)

#### publish.py
> #-*- coding: utf-8 -*-
> import paho.mqtt.client as mqtt
> import sys
> mqttc = mqtt.Client("python_pub")
> mqttc.connect("localhost", 1883)
> mqttc.publish("broker/messages", sys.argv[1])
> mqttc.loop(2) #timeout = 2s

#### Subscribe.py
> import paho.mqtt.client as mqtt
> #The callback for when the client receives a CONNACK response from the server.
> def on_connect(client, userdata, flags, rc):
>    print("Connected with result code "+str(rc))
>    #Subscribing in on_connect() means that if we lose the connection and
>    #reconnect then subscriptions will be renewed.
>    client.subscribe("broker/messages")
> #The callback for when a PUBLISH message is received from the server.
> def on_message(client, userdata, msg):
>     print(msg.topic+" "+str(msg.payload))
> client = mqtt.Client()
> client.on_connect = on_connect
> client.on_message = on_message
> client.connect("localhost", 1883, 60)
> #Blocking call that processes network traffic, dispatches callbacks and
> #handles reconnecting.
> #Other loop*() functions are available that give a threaded interface and a
> #manual interface.
> client.loop_forever()

#### In terminal line
	- python subscribe.py
	- pyhton publish.py “test”

# Mosquito Configuration Properties 
	
	- pid_file = contains the pid number. Simplifies the search of the process id.
	- persistence =If true, connection, subscription and message data will be written to the disk in mosquitto.db
	- persistence_location = indicates the location of the mosquitto.db 
	- allow_dupicate_messages = prevent to the client to receive the same message when it is subscribed to multiple topics that overlap. The broker keep track of the message. If disabled it, the clients should manage the duplicated messages.
	- persistent_client_expiration = indicates the time required for the broker to keep a client that 
	
	More properties here Mosquitto Config [link2](https://mosquitto.org/man/mosquitto-conf-5.html)
	More explanations here Mosquitto Doc [link3](https://mosquitto.org/man/mqtt-7.html)

