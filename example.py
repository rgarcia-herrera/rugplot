import numpy as np
from rugplot import CircleMarker, Scatter

N = 50
x = np.random.rand(N)
y = np.random.rand(N)

markers = [CircleMarker(x=x[i], y=y[i], r=2.5, fill='black', ) for i in range(N)]

s = Scatter(x, y, markers, insert=(100,30), size=(600,500))
s.drawBorder(stroke='grey', fill='white', stroke_width=0.4)
s.drawMarkers()
s.drawDotDash(['w','s'], dash_height=40, stroke="grey", stroke_width=0.4)
s.dwg.filename='example.svg'
s.dwg.save()
