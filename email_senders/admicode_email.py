import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email_senders import pillow_image as pic
from datetime import date


class EmailSender:
    def __init__(self):
        self.password = "rbigbysiscdvaljf"
        self.email = "developerstapsilogsystems3@gmail.com"
        self.smtp_port = 587
        self.smtp_server = "smtp.gmail.com"

    def send_code_email(self, name, code, person):
        self.subject = "HERE IS YOUR ADMIN CODE"
        self.body = f"""
        
Dear {name},

Thank you for choosing to register with TAPSILog SYSTEMS! We are delighted to have you on board.

As a part of our registration process, we require you to enter a registration code in order to complete your account setup. Please use the following code to register for our service: {code}.

To complete your registration, please follow the steps below:

-Visit our app and click on the "Register Admin" button.
-Enter your personal details, such as your name and email address.
-Enter the registration code we have provided above.

If you have any questions or concerns, please don't hesitate to contact our customer support team at {self.email}.

Thank you for choosing TAPSILog SYSTEMS and we look forward to serving you.

Best regards,

Kurt Russel Villamor (Kyna), The Creator
        
        
        """

        # Define Parts
        self.msg = MIMEMultipart()
        self.msg['From'] = self.email
        self.msg['To'] = person
        self.msg['Subject'] = self.subject

        # Attach file
        self.pic = pic.PicEdit(name, code)
        self.msg.attach(MIMEText(self.body, 'plain'))
        self.filename = f'email_senders/image_to_send/send{name}-{code}.png'
        self.attachment = open(self.filename, 'rb')

        # Base 64
        self.attachment_package = MIMEBase('application', 'octet-stream')
        self.attachment_package.set_payload((self.attachment).read())
        encoders.encode_base64(self.attachment_package)
        self.attachment_package.add_header('Content-Disposition', 'attachment; filename= ' + self.filename)
        self.msg.attach(self.attachment_package)

        self.text = self.msg.as_string()

        self.TIE_server = smtplib.SMTP(self.smtp_server, self.smtp_port)
        self.TIE_server.starttls()
        self.TIE_server.login(self.email, self.password)

        # SEND
        self.TIE_server.sendmail(self.email, person, self.text)
        print("Email Sent")


        self.TIE_server.quit()

    def send_qrHome(self, name, person):
        self.date = date.today()
        self.subject = f"HOMEOWNERS QR UPDATE TODAY {self.date.strftime('%B %d, %Y')}"
        self.body = f"""

Dear {name},
    
I hope this email finds you well. I am reaching out to provide you with the QR code necessary for entry into BARANGAY on {self.date.strftime('%B %d, %Y')}. Please find the attached QR code image file.

Please make sure to have the QR code readily available on your mobile device or printed out to present it at the designated entry point. Kindly note that without the QR code, access to the event/location/building may be denied.

If you have any questions or encounter any difficulties, please do not hesitate to contact me. I'll be happy to assist you.

Thank you for your cooperation, and I look forward to seeing you at SUBDIVISION.

Note: QR CODE EXPIRES WITHIN A DAY!

Best regards,

Kurt Russel Villamor (Kyna), The Creator

"""

        self.msg = MIMEMultipart()
        self.msg['From'] = self.email
        self.msg['To'] = person
        self.msg['Subject'] = self.subject

        # Attach file
        self.msg.attach(MIMEText(self.body, 'plain'))
        self.filename = f"qr_generate_scanner/qr_saves/HomeQr/QrHome{name}-{self.date.strftime('%m-%d-%Y')}.png"
        self.attachment = open(self.filename, 'rb')

        # Base 64
        self.attachment_package = MIMEBase('application', 'octet-stream')
        self.attachment_package.set_payload((self.attachment).read())
        encoders.encode_base64(self.attachment_package)
        self.attachment_package.add_header('Content-Disposition', 'attachment; filename= ' + self.filename)
        self.msg.attach(self.attachment_package)

        self.text = self.msg.as_string()

        self.TIE_server = smtplib.SMTP(self.smtp_server, self.smtp_port)
        self.TIE_server.starttls()
        self.TIE_server.login(self.email, self.password)

        # SEND
        self.TIE_server.sendmail(self.email, person, self.text)
        print("Email Sent")

        self.TIE_server.quit()

    def send_qrVisit(self, name, person):
            self.date = date.today()
            self.subject = f"VISITOR QR UPDATE TODAY {self.date.strftime('%B %d, %Y')}"
            self.body = f"""

    Dear {name},

    I hope this email finds you well. I am reaching out to provide you with the QR code necessary for entry into BARANGAY on {self.date.strftime('%B %d, %Y')}. Please find the attached QR code image file.

    Please make sure to have the QR code readily available on your mobile device or printed out to present it at the designated entry point. Kindly note that without the QR code, access to the event/location/building may be denied.

    If you have any questions or encounter any difficulties, please do not hesitate to contact me. I'll be happy to assist you.

    Thank you for your cooperation, and I look forward to seeing you at SUBDIVISION.

    Note: QR CODE EXPIRES WITHIN A DAY!

    Best regards,

    Kurt Russel Villamor (Kyna), The Creator

    """

            self.msg = MIMEMultipart()
            self.msg['From'] = self.email
            self.msg['To'] = person
            self.msg['Subject'] = self.subject

            # Attach file
            self.msg.attach(MIMEText(self.body, 'plain'))
            self.filename = f"qr_generate_scanner/qr_saves/VisitQr/QrVisit{name}-{self.date.strftime('%m-%d-%Y')}.png"
            self.attachment = open(self.filename, 'rb')

            # Base 64
            self.attachment_package = MIMEBase('application', 'octet-stream')
            self.attachment_package.set_payload((self.attachment).read())
            encoders.encode_base64(self.attachment_package)
            self.attachment_package.add_header('Content-Disposition', 'attachment; filename= ' + self.filename)
            self.msg.attach(self.attachment_package)

            self.text = self.msg.as_string()

            self.TIE_server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            self.TIE_server.starttls()
            self.TIE_server.login(self.email, self.password)

            # SEND
            self.TIE_server.sendmail(self.email, person, self.text)
            print("Email Sent")

            self.TIE_server.quit()

