import imaplib
import chardet
imapserver ="imap.qq.com"
emailuser="**************@qq.com"
emailpasswd="**************"
M = imaplib.IMAP4(imapserver,143)
M.login(emailuser,emailpasswd)
M.select('Inbox') 
typ, data = M.search('UNSEEN SINCE 01-Jan-2020')      
UIDS=data[0].split()[::-1]
print(UIDS)
if len(UIDS) >= 1:
    typ, data = M.fetch(UIDS[0], '(RFC822)')
    coding=chardet.detect(data[0][1])
    text = data[0][1].decode(encoding=coding["encoding"])
    message = email.message_from_string(text)  
    subject = message.get('subject')  
    Date = message.get('Date')  
    print(Date)  
    From = message.get('From')  
    print(From)  
    dh = email.header.decode_header(subject)
    de_text=dh[0][0]
    coding=dh[0][1]
    subject = de_text.decode(encoding=coding)
    print(subject)  
    for part in message.walk():
        type = part.get_content_type()
        disposition = str(part.get('Content-Disposition'))
        filename = part.get_filename()
        if type == 'text/plain' and 'attachment' not in disposition:
            with open("邮件正文内容.txt", 'wb') as f:
                f.write(part.get_payload(decode=True))
        elif filename:
            with open(filename,'wb') as f:
                f.write(part.get_payload(decode=True)) 
            print("下载"+filename)
M.close()
M.logout()
