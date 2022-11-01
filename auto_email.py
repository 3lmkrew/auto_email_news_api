import smtplib

gmail_app_pass = "zlenwdpvigzysjdp"


class EmailOut:

    def __init__(self, sender_email, receiver_email, subject, body):
        self.sender_email = sender_email
        self.receiver_email = receiver_email
        self.subject = subject
        self.body = body

    def send_me(self):
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(self.sender_email, gmail_app_pass)
            connection.sendmail(from_addr=self.sender_email,
                                to_addrs=self.receiver_email,
                                msg=f"Subject: {self.subject} \n\n {self.body}")
