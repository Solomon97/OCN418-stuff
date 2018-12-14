import requests
import datetime

url = 'https://tidesandcurrents.noaa.gov/api/datagetter?product=hourly_height&application=NOS.COOPS.TAC.WL&begin_date=20180729&end_date=20180824&datum=MLLW&station=1612480&time_zone=GMT&units=english&format=json'

df = requests.get(url)

df = df.json()
d = df['data']

DT = []
depth = []

for e in d:
    a = datetime.datetime.strptime(e['t'], '%Y-%m-%d %H:%M')
    v = float(e['v'])

    DT.append(a)
    depth.append(v)

import matplotlib.pyplot as plt

plt.plot_date(DT,depth, 'g:.')
plt.show()
