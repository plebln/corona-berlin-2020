#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


def fetch():
    dates = []
    values = []
    with open('virus-berlin-2020.dat') as fd:
        for line in fd.readlines():
            if line.strip().startswith('#'):
                continue
            words = line.split()
            if len(words) < 2:
                continue
            try:
                dates.append(int(words[1]))
                values.append(int(words[2]))
            except IndexError:
                print('FAILED:', line)
                continue
    return np.array(dates), np.array(values)


doys, values = fetch()
A = 3.0
r = 0.3
z = A * np.exp(r * (doys - 60))

fig = plt.figure()
plt.semilogy(doys, values, marker='o', label='Confirmed')
plt.semilogy(doys, z, linestyle="--", label='%g exp(%g [d - 60])' % (A, r))
plt.title('Coronavirus cases in Berlin')
plt.legend(loc='lower right')
plt.xlabel('Day in 2020')
plt.show()
