
import daytable

dt = daytable.DayTable('virus-germany-2020.dat')

delay = 7
for f in range(len(dt.dates)):
    if f < delay + 1:
        continue

    diff = dt.values[f] - dt.values[f-1]
    olddiff = dt.values[f - delay] - dt.values[f - delay - 1]

    print(dt.dates[f], dt.doys[f], dt.values[f], diff/olddiff)
