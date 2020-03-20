#!/usr/bin/env python3

import datetime
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def fetch(fname):
    dates = []
    doys = []
    values = []
    with open(fname) as fd:
        for line in fd.readlines():
            if line.strip().startswith('#'):
                continue
            words = line.split()
            if len(words) < 2:
                continue
            try:
                dates.append(words[0])
                doys.append(int(words[1]))
                values.append(int(words[2]))
            except IndexError:
                print('FAILED:', line)
                continue
    return np.array(dates), np.array(doys), np.array(values)


datestrs, doys, values = fetch('virus-berlin-2020.dat')
datetimes = []
for f in range(len(datestrs)):
    datetimes.append(datetime.datetime.strptime(datestrs[f], '%Y-%m-%d'))

dates = matplotlib.dates.date2num(datetimes)
A = 3.0
r = 0.3
z = A * np.exp(r * (doys - 60))

fig = plt.figure()
myFmt = matplotlib.dates.DateFormatter('%d.%m')
fig.gca().xaxis.set_major_formatter(myFmt)

plt.semilogy(doys-1, values, marker='o', label='Confirmed')
plt.semilogy(doys-1, z, linestyle="--", label='%g exp(%g [d - 60])' % (A, r))
plt.arrow(77-1, 60, 0, 240)
plt.text(76.7-1, 50, 'Schools closed', horizontalalignment='right')

bpop = 3748148    # Wikipedia, 31 Dec 2018
gpop = 831490300  # Wikipedia, 30 Sept 2019
gscale = bpop / gpop

gdates, gdoys, gvalues = fetch('virus-germany-2020.dat')
plt.semilogy(gdoys-1, gvalues * gscale, marker='x', label='Germany (scaled)')

plt.title('Confirmed coronavirus cases in Berlin and Germany (scaled)')
plt.legend(loc='lower right')
plt.xlabel('Date in 2020')
plt.show()
