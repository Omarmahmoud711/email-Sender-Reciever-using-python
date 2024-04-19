# Email Sender and Receiver

This project consists of two Python scripts: an email sender and an email receiver. The email sender script allows users to compose and send emails, while the email receiver script continuously monitors an email inbox and notifies the user when new emails are received.

## Features

- **Email Sender:**
  - Graphical user interface (GUI) application built with Tkinter.
  - Allows users to input email credentials, recipient email address, subject, message body, and optionally attach files.
  - Sends emails via Gmail's SMTP server using the `smtplib` library.

- **Email Receiver:**
  - Utilizes the IMAP protocol to connect to an email account and check for unseen emails in the inbox.
  - Runs continuously in a loop, periodically checking for new emails.
  - Displays desktop notifications using the `plyer` library when new emails are received.
  - Presents email content (sender, subject, and body) in a Tkinter message box.
  - Saves email attachments to the current directory and displays their filenames in the email content.

## Requirements

- Python 3.x
- `tkinter` library (included in standard Python distribution)
- `plyer` library (install using `pip install plyer`)

## Usage

1. **Email Receiver:**
   - Run the `Receiver.py` script.
   - make sure to provide the Reciever email address in the script manually 
   - Ensure that the script is running before sending emails from the sender script.
   - The receiver script will continuously monitor the specified email inbox and notify you when new emails are received.

2. **Email Sender:**
   - Run the `main.py` script for the sender.
   - Enter your email credentials, recipient email address, subject, message body, and optionally attach files.
   - Click the "Send Email" button to send the email.



