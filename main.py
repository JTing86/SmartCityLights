import threading
import sys
import paho.mqtt.client as mqtt
import serial
from lib import lib
import datetime
import time
import json
import requests

lib = lib(token="kWd5KDRgy-Y7Yy-QuNgfVRXcWACPTTfXC3N0EkIkL1mIF0VxtjpiGCsHUhMKIjgh")


def on_message(client, userdata, message):
    print(message.topic)
    msg = message.payload
    pos = [i-48 for i in msg]
    print(pos)
    pos = {'key': str(datetime.datetime.fromtimestamp(time.time())), 'value': [i for i in range(len(pos)) if pos[i] == 1]}
    if message.topic == "SmartStreet/Sensor":
        if pos['value']:
            results = requests.post("https://utils.lib.id/kv/set/", data=pos, headers={'Authorization': 'Bearer kWd5KDRgy-Y7Yy-QuNgfVRXcWACPTTfXC3N0EkIkL1mIF0VxtjpiGCsHUhMKIjgh'})
    elif message.topic == "SmartStreet/Fail":
        pos['value'] = 'There is a failure at position(s): ' + pos['value']
        results = requests.post("https://utils.lib.id/sms/", data={'to': '16466598166', 'body': pos['value']}, headers={'Authorization': 'Bearer kWd5KDRgy-Y7Yy-QuNgfVRXcWACPTTfXC3N0EkIkL1mIF0VxtjpiGCsHUhMKIjgh'})
        pos['table'] = 'StreetLightFailures'
        results = requests.post("https://utils.lib.id/kv/set/", data=pos, headers={'Authorization': 'Bearer kWd5KDRgy-Y7Yy-QuNgfVRXcWACPTTfXC3N0EkIkL1mIF0VxtjpiGCsHUhMKIjgh'})

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(topic='SmartStreet/Sensor')
    client.subscribe(topic='SmartStreet/Fail')

def on_publish(mosq, obj, mid):
    pass


def on_log(mqttc, userdata, level, string):
    print(string)

client = mqtt.Client()
client.on_message = on_message
client.on_publish = on_publish
# client.on_log = on_log
client.connect('test.mosquitto.org', 1883, 60)
client.subscribe([('SmartStreet/Sensor', 0), ('SmartStreet/Fail', 1)])
# client.subscribe()

client.loop_forever()
