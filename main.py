import smtplib
import tkinter as tk
from tkinter import filedialog, messagebox
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


class EmailApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Email Application")

        self.label_email = tk.Label(master, text="Email:")
        self.label_email.grid(row=0, column=0, sticky="e")
        self.entry_email = tk.Entry(master)
        self.entry_email.grid(row=0, column=1)

        self.label_password = tk.Label(master, text="Password:")
        self.label_password.grid(row=1, column=0, sticky="e")
        self.entry_password = tk.Entry(master, show="*")
        self.entry_password.grid(row=1, column=1)

        self.label_to = tk.Label(master, text="To:")
        self.label_to.grid(row=2, column=0, sticky="e")
        self.entry_to = tk.Entry(master)
        self.entry_to.grid(row=2, column=1)

        self.label_subject = tk.Label(master, text="Subject:")
        self.label_subject.grid(row=3, column=0, sticky="ne")
        self.entry_subject = tk.Entry(master)
        self.entry_subject.grid(row=3, column=1)

        self.label_message = tk.Label(master, text="Message:")
        self.label_message.grid(row=4, column=0, sticky="ne")
        self.text_message = tk.Text(master, height=5, width=30)
        self.text_message.grid(row=4, column=1)

        self.button_attach = tk.Button(master, text="Attach", command=self.attach_file)
        self.button_attach.grid(row=5, column=0, sticky="ne")

        self.button_send = tk.Button(master, text="Send Email", command=self.send_email)
        self.button_send.grid(row=5, column=1, sticky="ne")

    def attach_file(self):
        self.filename = filedialog.askopenfilename()
        if self.filename:
            self.attachment_label = tk.Label(self.master, text=f"Attachment: {self.filename}")
            self.attachment_label.grid(row=6, column=1, sticky="w")

    def send_email(self):
        try:
            smtp_server = 'smtp.gmail.com'
            smtp_port = 465  # SSL port
            sender_email = self.entry_email.get()
            password = self.entry_password.get()
            receiver_email = self.entry_to.get()
            subject = self.entry_subject.get()
            message = self.text_message.get("1.0", tk.END)

            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = receiver_email
            msg['Subject'] = subject

            msg.attach(MIMEText(message, 'plain'))

            if hasattr(self, 'filename'):
                with open(self.filename, 'rb') as attachment:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', f'attachment; filename={self.filename}')
                    msg.attach(part)

            with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, msg.as_string())

            messagebox.showinfo("Success", "Email sent successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")


def main():
    root = tk.Tk()
    app = EmailApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
