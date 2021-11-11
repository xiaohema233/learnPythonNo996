import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication 
From = '**************@163.com'
password = '**************'
To = ['**************@qq.com', '**************@21cn.com',
'**************@sina.com','**************@163.com']
smtpserver = 'smtp.163.com'
txtFile = '张小妹自荐信.txt'
imageFile = '张小妹简历.jpg'
docFile = '应聘投资经理岗位-XX大学-张小妹-金融-138xxxxxx78.doc'
pdfFile = '应聘投资经理岗位-XX大学-张小妹-金融-138xxxxxx78.pdf'
zipFile = '张小妹资料(简历+自荐信+照片).zip'
with open(txtFile,'r',encoding='utf-8') as f:
    textApart = MIMEText(f.read())
with open(imageFile,'rb') as f:
    imageApart = MIMEImage(f.read(),imageFile.split('.')[-1])   
    imageApart.add_header('Content-Disposition', 'attachment', filename=imageFile) 
with open(docFile,'rb') as f:
    docApart = MIMEApplication(open(docFile, 'rb').read())
    docApart.add_header('Content-Disposition', 'attachment', filename=docFile)
with open(pdfFile,'rb') as f:
    pdfApart = MIMEApplication(open(pdfFile, 'rb').read())
    pdfApart.add_header('Content-Disposition', 'attachment', filename=pdfFile)
with open(zipFile,'rb') as f:
    zipApart = MIMEApplication(open(zipFile, 'rb').read())
    zipApart.add_header('Content-Disposition', 'attachment', filename=zipFile)
message = MIMEMultipart()
message.attach(textApart)
message.attach(imageApart)
message.attach(docApart)
message.attach(pdfApart)
message.attach(zipApart)
message['Subject'] = '应聘投资经理岗位-XX大学-张小妹-金融-138xxxxxx78'
server = smtplib.SMTP_SSL(smtpserver,465)
server.login(From,password)
server.sendmail(From, To, message.as_string())
server.quit()
