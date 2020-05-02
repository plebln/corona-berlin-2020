
import daytable
import sys

if len(sys.argv) != 2:
	print('Usage: {command} {history file}')
	raise Exception

dt = daytable.DayTable(sys.argv[1])

delay = 7
for f in range(delay + 1, len(dt.dates) - 1):
    # Centered difference
    rate = (dt.values[f+1] - dt.values[f-1]) / dt.values[f]
    oldrate = (dt.values[f - delay + 1] - dt.values[f - delay - 1]) \
        / dt.values[f - delay]

    print(dt.dates[f], dt.doys[f], dt.values[f], rate/oldrate)
