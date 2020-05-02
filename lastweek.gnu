set xdata time
set timefmt "%Y-%m-%d"
set st da linespoints
set xra ["2020-04-17":]
set key top left
plot 'virus-berlin-2020-week.dat' u 1:4, 1, 'virus-germany-2020-week.dat' u 1:4

