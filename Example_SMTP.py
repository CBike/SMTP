import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



def smtp_setting(email, password):
    mailserver = ''
    port = 00

    smtp = smtplib.SMTP(mailserver, port)
    smtp.set_debuglevel(True)

    smtp.ehlo()
    smtp.starttls()
    smtp.login(email, password)

    return smtp

def send_plain_mail(sender, recevier, email, password, subject, content):
    try:
        smtp = smtp_setting(email, password)
        msg = MIMEText(content)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = recevier

        smtp.sendmail(sender, recevier, msg.as_string())


    except Exception as e:
        print('error:',e)

    finally:
        if smtp is not None:
            smtp.quit()

if __name__ == '__main__':


    sender = str('')
    password = str('')
    receiver = str('')

    smtp_setting(sender, password)
    send_plain_mail(sender, receiver, sender, password, 'TEST(subject)', 'TEST(content)')