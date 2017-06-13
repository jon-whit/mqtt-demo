import paho.mqtt.client as mqtt
import argparse

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    client.subscribe("home/kitchen/temp")

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

parser = argparse.ArgumentParser()
parser.add_argument("--host", metavar='<host>', required=True, help="The MQTT broker hostname.")
parser.add_argument("--port", metavar='<port>', type=int, default=1883, help="The MQTT broker port.")
parser.add_argument("--topic", metavar='<topic>', required=True, help="The MQTT topic to subscribe to.")

args = parser.parse_args()

# Create the MQTT client
client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect(args.host, args.port)

# Blocking call that processes network traffic, dispatches callbacks
# and handles reconnecting.
# 
# Other loop*() functions are available that give threaded interfaces.
client.loop_forever()

