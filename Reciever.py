import imaplib
import email
import tkinter as tk
from tkinter import messagebox
from plyer import notification
import os

class EmailReceiver:
    def __init__(self):
        self.imap_host = 'outlook.office365.com'
        self.imap_port = 993
        self.username = 'enter your outlook email here for the reciever '
        self.password = 'and the password'
        self.root = tk.Tk()
        self.root.withdraw()  # Hide the main window

    def check_emails(self):
        try:
            # Connect to the IMAP server
            mail = imaplib.IMAP4_SSL(self.imap_host, self.imap_port)
            # Login to the email account
            mail.login(self.username, self.password)
            mail.select('inbox')

            # Search for unseen emails
            status, data = mail.search(None, 'UNSEEN')

            if status == 'OK':
                for num in data[0].split():
                    # Fetch the email message
                    status, msg_data = mail.fetch(num, '(RFC822)')
                    if status == 'OK':
                        raw_email = msg_data[0][1]
                        msg = email.message_from_bytes(raw_email)
                        self.show_notification(msg)
            mail.close()
            mail.logout()
        except Exception as e:
            print("Error:", e)

    def show_notification(self, msg):
        # Display notification
        notification.notify(
            title="New Email Received",
            message="You've received a new email!",
            timeout=5
        )

        # Display email content using tkinter
        messagebox.showinfo("New Email", f"From: {msg['From']}\nSubject: {msg['Subject']}\n\n{self.get_email_body(msg)}")

    def get_email_body(self, msg):
        email_body = ""
        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                if content_type == 'text/plain':
                    email_body += part.get_payload(decode=True).decode('utf-8')
                elif content_type == 'text/html':
                    pass  # Ignore HTML emails
                elif 'attachment' in content_type:
                    filename = part.get_filename()
                    if filename:
                        attachment_path = os.path.join(os.getcwd(), filename)
                        with open(attachment_path, 'wb') as f:
                            f.write(part.get_payload(decode=True))
                        email_body += f"\nAttachment: {filename}"
        else:
            email_body = msg.get_payload(decode=True).decode('utf-8')
        return email_body

def main():
    receiver = EmailReceiver()
    while True:
        receiver.check_emails()

if __name__ == "__main__":
    main()
