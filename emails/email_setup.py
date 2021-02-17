"""
Deals with email backend

Not the most secure method for storing passwords, but better than hard-coding them in this file...

AUTHENTICATION_FILE should be in format:
    server_email, abc@gmail.com
    server_password, abc_abc
    receiver_email, bca@gmail.com
    port, 465

Be careful with the .gitignore ...
"""
import os
import smtplib
import ssl

AUTHENTICATION_FILE = "email_server_credentials.txt"


class Email:
    def __init__(self):
        # Trap for young players: relative vs absolute paths
        current_directory = os.path.dirname(os.path.abspath(__file__))
        auth_file = os.path.join(current_directory, AUTHENTICATION_FILE)

        with open(auth_file, "r") as fp:
            details = {}
            for row in fp.readlines():
                columns = row.split(",")
                # fields shouldn't have any spaces
                details[columns[0]] = columns[1].strip()
        self.server_email = details['server_email']
        self.server_password = details['server_password']
        self.receiver_email = details['receiver_email']
        self.port = details['port']

    def send_email(self, message: str, subject: str):
        message = f'Subject: {subject}\n' + message
        context_socket = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", self.port, context=context_socket) as server:
            server.login(self.server_email, self.server_password)
            server.sendmail(self.server_email, self.receiver_email, message.encode("ascii", "replace"))
