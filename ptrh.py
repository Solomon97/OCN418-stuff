from node.drivers.bme280 import BME280
import time
import json

f = open('temphumP.csv', 'a')

bme = BME280(address=0x76)

re = bme.read()
ts = time.time()
temp = re['t']
hum = re['rh']
pre = re['p']
header = "{:>15}\t{:>7}\t{:>7}\t{:>7}\n".format('ts', 'pre', 'temp', 'hum')
line = "{:>10}\t{:>5}\t{:>5}\t{:>5}\n".format(ts, pre, temp, hum)

print(header)

while True:
    f.write(line)
    f.flush()
    print(line)
    time.sleep(1)
f.close()

