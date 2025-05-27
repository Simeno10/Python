from tkinter import *
from time import *
import smtplib


def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)
    day_string = strftime("%A")
    day_label.config(text=day_string)
    date_string = strftime("%B %d %Y")
    date_label.config(text=date_string)

    window.after(1000,update)

sender = "***********@**********.***"
receiver = "simeno10@gmail.com"
password = "************************"
subject = "Python email test"
body = "Yoooooooo!"
try:
    message = f"""From: Snoop Dogg{sender}
    To: Nicolas Cage{receiver}
    Subject: {subject}\n
    {body}
    """
except smtplib.SMTPAuthenticationError:
    print("unable to sign in")

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

server.login(sender,password)
print("Logged in...")
server.sendmail(sender,receiver,message)
print("Email has been sent!")

window = Tk()

time_label = Label(window, font=("Arial", 50), fg="blue", bg="black")
time_label.pack()

day_label = Label(window, font=("Ink Free", 25))
day_label.pack()

date_label = Label(window, font=("Modern", 30))
date_label.pack()

update()

window.mainloop()