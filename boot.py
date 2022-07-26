import time
from umqttsimple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp
esp.osdebug(None)
import gc
gc.collect()

ssid = 'username'
password = 'password'
mqtt_server = '3.120.232.128'
#EXAMPLE IP ADDRESS
#mqtt_server = '192.168.1.144'
client_id = ubinascii.hexlify(machine.unique_id())
topic_sub = b'notification'
topic_pub = b'GasSensorData'

last_message = 0
message_interval = 0
counter = 0

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

adc = machine.ADC(0) 

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())


