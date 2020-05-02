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

future_days = 10  # May 1 ???
horizon = doys[-1] + future_days  # Look no further than this into the future.
print('Most recent day', datetimes[-1])
horizon_datetime = datetimes[-1] + datetime.timedelta(future_days, 0, 0, 0)
#
print('Horizon:', horizon_datetime)

doys_z = np.linspace(60, 102, 43)  # Just to 2020-04-11 = doy 102, predicts 900k then.
z = A * np.exp(r * (doys_z - 60))
print('On', doys_z[-1], 'predict', int(z[-1]))

A_2 = 900   # n(doy=080) was 868
r_2 = 0.12
doys_z2 = np.linspace(80, horizon)
z_2 = A_2 * np.exp(r_2 * (doys_z2 - 80))
print('On', horizon_datetime, 'predict', int(z_2[-1]))

A_3 = 4500
r_3 = 0.04
doys_z3 = doys_z2
z_3 = A_3 * np.exp(r_3 * (doys_z3 - 102))
print('On', horizon_datetime, 'predict', int(z_3[-1]))

fig = plt.figure()
gs = matplotlib.gridspec.GridSpec(nrows=2, ncols=1, height_ratios=[3,1])

myFmt = matplotlib.dates.DateFormatter('%d.%m')

ax0 = fig.add_subplot(gs[0,0])
ax0.xaxis_date()
ax0.xaxis.set_major_formatter(myFmt)

ax0.set_ylim([2, 9000])
ax0.plot(doys-1, values, marker='o', label='Confirmed')
ax0.plot(doys_z-1, z,
         linestyle="-.", label='%g exp(%g [d - 60])' % (A, r))
ax0.plot(doys_z2-1, z_2,
         linestyle="--", label='%g exp(%g [d - 80])' % (A_2, r_2))
ax0.plot(doys_z3-1, z_3,
         linestyle="--", label='%g exp(%g [d - 102])' % (A_3, r_3))


ax0.arrow(77-1, 60, 0, 240)
ax0.text(76.7-1, 30, 'Schools closed', horizontalalignment='center')
ax0.arrow(82-1, 800 - 500, 0, 500)
ax0.text(82-1+2, 200, '"Lockdown"', horizontalalignment='left')
# Easter, 2020-04-12 = doy 103
ax0.arrow(103-1, 4500 - 3000, 0, 3000)
ax0.text(103-1, 1200, 'Easter', horizontalalignment='center')


bpop =  3748148    # Wikipedia, population of Berlin, at 31 Dec 2018
gpop = 83149030    # Wikipedia, population of Germany, at 30 Sept 2019
gscale = bpop / gpop

gdates, gdoys, gvalues = fetch('virus-germany-2020.dat')
ax0.plot(gdoys-1, gvalues * gscale, marker='x', label='Germany (scaled)')
ax0.legend(loc='upper left')

plt.title('Confirmed coronavirus cases in Berlin and Germany (scaled)')

rdelta = np.zeros(len(doys))
for j in range(3, len(doys)):
    rdelta[j] = 100.0 * (values[j] - values[j-1]) / values[j-1]

ax1 = fig.add_subplot(gs[1,0])
ax1.xaxis_date()
ax1.xaxis.set_major_formatter(myFmt)

ax1.plot(doys[0:]-1, rdelta[0:], 'bo')
ax1.set_xlim([doys[0]-2, horizon])
ax1.set_ylim([0, 20])
ax1.set_title('Relative daily increase (%)')
plt.xlabel('Date in 2020')


plt.show()
