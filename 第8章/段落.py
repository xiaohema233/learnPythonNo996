txt_0='什么是汽车金融？'
txt_1='''汽车金融是汽车全产业链覆盖的资本流动。狭义的汽车金融隶属于消费金融,广义的汽车金融贯穿全产业链。汽车金融的概念最早源于美国，狭义的汽车金融，更多地关注汽车销售环节，为下游客户提供融资性金融服务,隶属于消费金融。广义的汽车金融，是贯穿汽车的生产、流通、销售、使用回收等环节中的资金流动，提高资本利用率和资金周转率。'''
txt_2='''我国汽车消费金融业萌芽于商业银行贷款，后经政策放宽，形成汽车金融公司、汽车融资租赁公司、互联网汽车金融公司等多元主体并存的局面。'''
txt_3='''中国汽车消费金融渗透率与海外成熟市场差距很大。汽车金融的渗透率，指通过贷款、融资等金融方式购买的车辆数量与汽车销量之比。中国汽车消费金融渗透率一直处于较低水平。'''


from reportlab.lib.styles import getSampleStyleSheet
s = getSampleStyleSheet()
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
pdfmetrics.registerFont(TTFont('微软雅黑', 'msyh.ttf'))
s["Title"].fontName,s["Title"].fontSize='微软雅黑' ,30
s["Title"].spaceAfter,s["Normal"].spaceBefore=30,10
s["Normal"].fontName,s["Normal"].fontSize='微软雅黑',20
s["Normal"].leading= 30
s["Normal"].firstLineIndent = 40
from reportlab.platypus import Paragraph
p_0=Paragraph(txt_0,s["Title"])
p_1=Paragraph(txt_1,s["Normal"])
p_2=Paragraph(txt_2,s["Normal"])
p_3=Paragraph(txt_3,s["Normal"])
from reportlab.platypus import SimpleDocTemplate
doc = SimpleDocTemplate(r'H:\示例\第8章\mydoc.pdf',pagesize=(1200,800))
story_text = [p_0,p_1,p_2,p_3]
doc.build(story_text)