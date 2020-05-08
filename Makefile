all: virus-berlin-2020-week.dat virus-germany-2020-week.dat figure_1.png

figure_1.png: plot.py virus-berlin-2020.dat
	python3 plot.py

virus-berlin-2020-week.dat: lastweek.py virus-berlin-2020.dat
	python3 lastweek.py virus-berlin-2020.dat >$@

virus-germany-2020-week.dat: lastweek.py virus-germany-2020.dat
	python3 lastweek.py virus-germany-2020.dat >$@

