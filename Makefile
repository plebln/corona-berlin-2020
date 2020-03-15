all: figure_1.png

figure_1.png: plot.py virus-berlin-2020.dat
	python3 plot.py

