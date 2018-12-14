from tcs34725 import TCS34725 as lgt
import time


sensor = lgt()
sensor.gain(60)
sensor.integration_time(101)

f = open('bill.csv', 'a')


while True:
    r = sensor.read()
    line = '{},{:.4f},{:.4f},{:.4f}\n'.format(time.time(), r['r'], r['g'], r['b'])
    print(line)
    time.sleep(60)

    f.write(line)
    f.flush()

f.close()


#'{},{},{}'.format(1,2,3)
#print(r['r'],r['g'], r['b'])
