import smtplib

class SendMail:
    def send(self, receiver_email_id):
        try:
            user_email_id = 'v.subramanyam586@gmail.com'
            user_password = 'SUBramanyam@123'
            s= smtplib.SMTP('smtp.gmail.com',587)
            s.starttls()
            s.login(user_email_id,user_password)
            message = 'Thanks for Shopping, Visit Once Again'
            s.sendmail(user_email_id, receiver_email_id, message)
            s.quit()
        except Exception as e:
            print(e)