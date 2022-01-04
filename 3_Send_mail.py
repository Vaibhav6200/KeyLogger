import smtplib

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)


email = "test@gmail.com"
password = "Test123"
message = "hey there how are you"
send_mail(email, password, message)