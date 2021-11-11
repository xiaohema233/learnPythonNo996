import imapclient
import pyzmail
imapserver ="imap.qq.com"
emailuser="**************@qq.com"
password="**************"
M = imapclient.IMAPClient(imapserver,ssl=True)
M.login(emailuser,password)
M.select_folder('INBOX',readonly=True)
UIDS = M.search('UNSEEN SINCE 01-Jan-2020')
if len(UIDS) >= 1:
    UID=UIDS[len(UIDS)-1]
    rawMessage = M.fetch(UID,[b'BODY[]'])
    message = pyzmail.PyzMessage.factory(rawMessage[UID][b'BODY[]'])
    print(message.get_subject())
    print(message.get_addresses('from')[0][1])
    for part in message.mailparts:
        if part.filename:
            with open(part.filename, 'wb') as f:
                f.write(part.get_payload())
        else:
            with open("邮件正文内容.txt", 'wb') as f:
                f.write(part.get_payload())
M.logout()
