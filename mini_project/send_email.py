import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import os
from mini_project import error_logger

class Transaction_email:
    def __init__(self):
        self.from_email_address = 'python.developer.subramanyam@gmail.com'
        self.from_email_password = 'SUBramanyam@123'
        self.files_dir = 'pdf_files/'
        self.error_log = error_logger.ReportError()

    def send_mail(self, to_email_address, file_name, customer_name,transaction_id):
        try:
            msg = MIMEMultipart()
            msg['From'] = self.from_email_address
            msg['To'] = to_email_address
            msg['Subject'] = 'Bill Statement'
            body = 'Thanks you {} For Shopping with us, Please visit again, Please find attached transaction details in the document with the transaction id : {}'.format(customer_name,transaction_id)
            msg.attach(MIMEText(body, 'plain'))
            attachment = open(str(os.path.abspath(file_name)), 'rb')

            # Instance of MIMEBase and names as p
            p = MIMEBase('application', 'octet-stream')

            # To change the payload into ecoded form
            p.set_payload((attachment).read())

            # encode into base64
            encoders.encode_base64(p)

            p.add_header('Content-Disposition', 'attachment; filename= %s' % file_name)

            # Attach Instance 'p' to Instance 'msg'
            msg.attach(p)

            # create SMTP session
            s = smtplib.SMTP('smtp.gmail.com', 587)

            # Start TLS for Security
            s.starttls()

            # Authentication
            s.login(self.from_email_address, self.from_email_password)

            # Convert Multiport message into a String
            text = msg.as_string()

            # sending the email
            s.sendmail(self.from_email_address, to_email_address, text)

            # Terminating the session
            s.quit()
        except Exception as e:
            self.error_log.report_error_log(__file__, e.__str__())
