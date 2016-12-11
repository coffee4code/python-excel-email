#!/usr/bin/python

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Client:

    _msg = ''

    server_name = ''
    server_port = ''
    server_debug = ''

    sender_email = ''
    sender_password = ''

    mail_subject = ''
    mail_message_text = ''
    mail_message_html = ''

    targets = []

    def __init__(self):
        self._msg = MIMEMultipart('alternative')

        self.server_name = ''
        self.server_port = ''
        self.server_debug = ''

        self.sender_email = ''
        self.sender_password = ''

        self.mail_subject = ''
        self.mail_message_text = ''
        self.mail_message_html = ''

        self.targets = []

    def _build(self):
        self._msg['From'] = self.sender_email
        self._msg['To'] = ", ".join(self.targets)
        self._msg['Subject'] = self.mail_subject

        part1 = MIMEText(self.mail_message_text, 'plain')
        part2 = MIMEText(self.mail_message_html, 'html')

        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best and preferred.
        self._msg.attach(part1)
        self._msg.attach(part2)

    def server(self, server, port, debug):
        self.server_name = server
        self.server_port = port
        self.server_debug = debug

    def auth(self, email, password):
        self.sender_email = email
        self.sender_password = password

    def subject(self, subject):
        self.mail_subject = subject

    def message_text(self, text):
        self.mail_message_text = text

    def message_html(self, html):
        self.mail_message_html = html

    def receiver(self, target):
        self.targets.append(target)

    def send(self):

        self._build()

        server = smtplib.SMTP_SSL(self.server_name, self.server_port)
        server.set_debuglevel(self.server_debug)
        server.login(self.sender_email, self.sender_password)
        server.sendmail(self.sender_email, self.targets, self._msg.as_string())
        server.quit()

