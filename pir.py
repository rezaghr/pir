#hi man 
#this app for conect pir sensor to raspberry pi 
#this app email you 
#in this app i use GPIO 18
#you can conect out pin to any GPIO but you mast now GPIO coe
#for this you mast whrite pinout in raspberry pi terminal
#you can conect me in telegram @rezaghrr

#import 
import time
import RPi.GPIO as GPIO
import smtplib
#set mode
GPIO.setmode(GPIO.BCM)
# turn gpio pin on
GPIO.setup(18, GPIO.IN)
#create fanction
def email():
  server = smtplib.SMTP(‘smtp.gmail.com’, 587)
	server.starttls()
	server.login('your gmail', 'your password')
  msg = ("harkat yaft shod")
	email = ('motion detected')
	server.sendmail('inter your mail here', email, msg)
	server.quit()


# create while loop
While True:
	Input_state = GPIOinput(18)
              if input_state == True:
                email()
                time.sleep(2)
