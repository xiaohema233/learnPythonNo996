import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import imapclient,pyzmail
import time,os
from PIL import ImageGrab
def sendmail(smtpserver,emailuser,emailpasswd,To,subject):
    time_now = time.strftime('%Y%m%d-%H%M%S')
    pic = ImageGrab.grab()
    imageFile = time_now+'.jpg'
    pic.save(imageFile)
    message = MIMEMultipart()
    with open(imageFile,'rb') as f:
        imageApart = MIMEImage(f.read(),imageFile.split('.')[-1])   
        imageApart.add_header('Content-Disposition', 'attachment', filename=imageFile) 
    message.attach(imageApart)
    print("开始发送邮件"+subject)
    message['Subject'] = subject
    server = smtplib.SMTP(smtpserver)
    server.login(emailuser,emailpasswd)
    server.sendmail(emailuser, To, message.as_string())
    server.quit()
def getmail(smtpserver,emailuser,emailpasswd):
    imapObj = imapclient.IMAPClient(imapserver,ssl=True)
    imapObj.login(emailuser,emailpasswd)
    imapObj.select_folder('INBOX',readonly=True)
    UIDS = imapObj.search('UNSEEN SINCE 01-Jan-2020')
    if len(UIDS) >= 1:
        rawMsg = imapObj.fetch(UIDS[len(UIDS)-1],[b'BODY[]'])
        Msg = pyzmail.PyzMessage.factory(rawMsg[UIDS[len(UIDS)-1]][b'BODY[]'])
        subject=Msg.get_subject()
    else:
        subject="未收到信息"
    imapObj.logout()
    return subject
if __name__=='__main__':
    smtpserver ="smtp.qq.com"
    imapserver ="imap.qq.com"
    emailuser="**************@qq.com"
    emailpasswd="**************"
    To="**************@sina.com"
    while True:
        subject=getmail(imapserver,emailuser,emailpasswd)
        print("收到信息"+subject)
        if subject[0:4] == '远程指令':
            cmd = subject[5:]
            try:
                os.system(cmd)  
                sendmail(smtpserver,emailuser,emailpasswd,To,"完成指令"+cmd) 
            except:
                os.system('echo error')
                sendmail(smtpserver,emailuser,emailpasswd,To,'echo error') 
            break
        time.sleep(120)
