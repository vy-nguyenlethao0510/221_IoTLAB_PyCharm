import sys
from Adafruit_IO import MQTTClient
import time
import random
from ai import *
from uart import *

AIO_FEED_IDs = ["sensor1", "sensor2", "sensor3", "button1", "button2"]
AIO_USERNAME = ""
AIO_KEY = ""

def connected(client):
    print("Connection has been established.")
    for feed in AIO_FEED_IDs:
        client.subscribe(feed)

def subscribe(client , userdata , mid , granted_qos):
    print("Finish subscribing.")

def disconnected(client):
    print("Disconnecting...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Receive data: " + payload)
    if feed_id == "button1":
        if payload == "0":
            writeData("1")
        else:
            writeData("2")
    if feed_id == "button2":
        if payload == "0":
            writeData("3")
        else:
            writeData("4")

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

counter = 10
counter_ai = 5
prev_ai = 2

while True:
    # counter = counter - 1
    # if counter <= 0:
    #     counter = 10
    #     print("Publishing random data...")
    #     temp = random.randint(20, 30)
    #     client.publish("sensor1", temp)
    #     bright = random.randint(60, 80)
    #     client.publish("sensor3", bright)
    #     humid = random.randint(40, 50)
    #     client.publish("sensor3", humid)

    # counter_ai = counter_ai - 1
    # if counter_ai <= 0:
    #     counter = 5
    #     ai_result = ai_func()
    #     if ai_result != prev_ai:
    #         prev_ai = ai_result
    #         print("AI output: ", ai_result)
    #         client.publish("ai", ai_result)

    readSerial(client)

    time.sleep(1)
    pass