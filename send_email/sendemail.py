import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
class EmailNotification:

    def send_email(self):
        msg = MIMEMultipart()
        msg['From'] = 'advaithab1513@gmail.com'
        msg['To'] = 'mallikarjuna.b@mitel.com'
        msg['Subject'] = "Test Results Email"
        body = "Test Results Email Summary"
        msg.attach(MIMEText(body, 'plain'))
        path = "C:\\Users\\mallikar\\Documents\\Python_Workspace\\PM_SNM_Project\\tests\\results.html"
        fileName = "results.html"
        attachment = open(path, 'rb')
        p = MIMEBase('application','octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % fileName)
        msg.attach(p)
        smtpobj = smtplib.SMTP("smtp.gmail.com", 587)
        smtpobj.ehlo()
        smtpobj.starttls()
        smtpobj.login("advaithab1513@gmail.com", "RohiArjun@123")
        message = "This is a test email"
        text = msg.as_string()
        smtpobj.sendmail("advaithab1513@gmail.com", "karthik.nanjundaiah@mitel.com", text)
        smtpobj.quit()

x = EmailNotification()
x.send_email()


"""
# list of email_id to send the mail 
li = ["xxxxx@gmail.com", "yyyyy@gmail.com"] 
  
for i in range(len(li)): 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login("sender_email_id", "sender_email_id_password") 
    message = "Message_you_need_to_send"
    s.sendmail("sender_email_id", li[i], message) 
    s.quit() 

"""