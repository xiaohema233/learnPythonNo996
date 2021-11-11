from reportlab.graphics.shapes import Drawing
d = Drawing(100, 100)
from reportlab.graphics.charts.barcharts import VerticalBarChart
bar = VerticalBarChart()
bar.x,bar.y,bar.height,bar.width,bar.valueAxis.valueMin=50,-150,280,500,0
bar.categoryAxis.categoryNames=['2012','2013','2014','2015','2016']
bar.data = [[16, 17, 18, 24, 25]]
bar.bars[0].fillColor,bar.barLabels.nudge=colors.black,18
bar.barLabelFormat,bar.valueAxis.labels.fontSize='%0.0f',20
bar.categoryAxis.labels.fontSize,bar.barLabels.fontSize=20,30
d.add(bar)
from reportlab.platypus import Spacer
story_chart=[Spacer(1,75),d]
from reportlab.platypus import SimpleDocTemplate
doc = SimpleDocTemplate(r'H:\示例\第8章\mydoc_chart.pdf',pagesize=(1200,800))
doc.build(story_chart)
