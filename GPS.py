import serial
import time


s = serial.Serial('/dev/ttyS0',9600)
f = open('loc.csv', 'a')

while True:
    gps = str(s.readline())
    if gps.find('GPGGA') > 0:
        r = gps.strip().split(',')
        lat = r[2]
        ns = r[3]
        lon = r[4]
        we = r[5]
        ts = time.time()
        location = "{},{},{},{},{}\n".format(ts,lat,ns,lon,we)
        print(location)
        f.write(location)
        f.flush()
f.close()
        
