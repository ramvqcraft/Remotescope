from time import sleep
import RPi.GPIO as GPIO

EN = 25
DIR = 14
PUL = 15
#delay = 0.01 
#delay = 0.002 #works
#delay = 0.001#works
#delay = 0.0005#works
#delay = 0.0001#works


GPIO.setmode(GPIO.BCM)
GPIO.setup(PUL, GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(EN, GPIO.OUT)

GPIO.output(DIR, GPIO.LOW)
GPIO.output(EN, GPIO.HIGH)

while(1==1):
	
	GPIO.output(PUL, GPIO.HIGH)
	sleep(delay)
	GPIO.output(PUL, GPIO.LOW)
	sleep(delay)
