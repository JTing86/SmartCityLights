import random
import paho.mqtt.client as mqtt
import time
import serial
import threading

total_lights=60

current_state = [0 for i in range(total_lights)]

def run_out(new_state):
    for i in new_state:
        current_state[i] = 0
    arduino = serial.Serial(port="COM4", baudrate=9600)
    print(bytearray(current_state))
    arduino.write(bytearray(arduino))
    arduino.close()

def activetoOneHot(active_sensors, total_lights=total_lights, total_sensors=6, overlap=3):
    pos_to_turn_light_on = []
    sensorsToLightsConversion = int(total_lights / total_sensors)
    for k in active_sensors:
        lowest_index = (k * sensorsToLightsConversion - overlap) if (k * sensorsToLightsConversion - overlap) > 0 else 0
        higher_index = k * sensorsToLightsConversion + sensorsToLightsConversion + overlap
        pos_to_turn_light_on.extend([i for i in range(lowest_index, higher_index)])
    pos_to_turn_light_on.sort()
    t = threading.Timer(5, run_out, [pos_to_turn_light_on])
    return t, pos_to_turn_light_on

def on_message(client, userdata, message):
    msg = message.payload
    pos = [i-48 for i in msg]
    pos = [i for i in range(len(pos)) if pos[i] == 1]
    global current_state
    timer, new_state = activetoOneHot(pos)
    for i in new_state:
        current_state[i] = 1
    print(current_state)
    arduino = serial.Serial(port="COM4", baudrate=9600)
    print(bytearray(current_state))
    arduino.write(bytearray(arduino))
    arduino.close()
    timer.start()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(topic='SmartStreet/Sensor')

def on_publish(mosq, obj, mid):
    pass


def on_log(mqttc, userdata, level, string):
    print(string)

client = mqtt.Client()
client.on_message = on_message
client.on_publish = on_publish
# client.on_log = on_log
client.connect('test.mosquitto.org', 1883, 60)
client.subscribe('SmartStreet/Sensor', 0)

client.loop_forever()