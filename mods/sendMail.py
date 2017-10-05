from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def sendMail(thelist): #Sends Emails Based on What's in List: Make it check for IP, add different email options
    me = "yohance.clarkii@enlitellc.com"
    you = "yohance.clarkii@enlitellc.com"


    msg = MIMEMultipart()
    msg["From"] = me
    msg["to"] = you
    msg["Subject"] = "Your IP ADDRESSES"

    body = "Your Raspberry Pi's IP Address is: %s\nYour Raspberry Pi's Public IP is: %s" % (thelist[0],thelist[1])
    msg.attach(MIMEText(body, "plain"))
    print(body)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(me,"12345678")
    text = msg.as_string()
    server.sendmail(me,you,text)
    server.quit()
