#!/usr/bin/env python3

import numpy as np

class DayTable(object):

  def __init__(self, fname):
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
    self.dates = np.array(dates)
    self.doys = np.array(doys)
    self.values = np.array(values)


