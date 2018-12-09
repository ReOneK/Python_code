from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF

data = [
    (2018, 8, 113.2, 114.2, 112.2),
    (2018, 9, 112.2, 114.2, 122.2),
    (2018, 10, 123.2, 114.2, 112.2),
    (2018, 7, 113.2, 124.2, 112.2),
    (2018, 5, 123.2, 114.2, 112.2),
    (2018, 2, 113.2, 124.2, 122.2),
]


drawing = Drawing(200, 150)


pred = [raw[2]-40 for raw in data]
high = [raw[3]-40 for raw in data]
low = [raw[4]-40 for raw in data]
times = [200*((raw[0]+raw[1]/12.0)-2018)-110 for raw in data]

drawing.add(PolyLine(list(zip(times, pred)), strokeColor=colors.blue))
drawing.add(PolyLine(list(zip(times, high)), strokeColor=colors.red))
drawing.add(PolyLine(list(zip(times, low)), strokeColor=colors.green))
drawing.add(String(65, 115, 'Test', fontSize=18, fillColor=colors.red))

renderPDF.drawToFile(drawing, 'report.pdf', 'Test')