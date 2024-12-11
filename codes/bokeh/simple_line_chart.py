from turtle import color
from bokeh.plotting import figure, show
from matplotlib import legend

x=[1,2,3,4,5]
y=[6,7,2,4,5]
z=[2,3,4,5,6]
a=[4,5,5,7,2]

p=figure(title='Simple line chart', x_axis_label='x', y_axis_label='y')

p.line(x,y,legend_label='Temp.', line_width=2, color='blue')
p.line(x,z,legend_label='Rate', line_width=2, color='red')
p.line(x,a,legend_label='Objects', line_width=2, color='green')

show(p)