#!/usr/bin/env python2
#import all the libraries and elements that we need
import time
import sys
import RPi.GPIO as GPIO
#import CloudFunctions

#turn off meaningless warnings
GPIO.setwarnings(False)

#define global variables defaults
LED_FREQ = 120	#frequency of LED PWM switching
LOCATION = "CAXX0518"	#location of the weather we want
MODE = "mirror"	#mode we want to be in (default is mirror weather at location)

#open the settings file and grab all our globals from there
config = open("settings.conf", "r")
line = config.readline()
print "Line Read: %s" % (line)
line = config.readline()
print "Line Read: %s" % (line)
line = config.readline()
print "Line Read: %s" % (line)

#define all the functions we need in the program
#function to start all the pins with current duty cycle
def startLeds( leds, duty_cycles ):
	"Function turns on all LEDs in array of LED objects provided"
	print "\nStarting all LEDs!"
	for index in range(len(leds)):
		leds[index].start(duty_cycles[index])
	return

#function to stop all pins
def stopLeds( leds ):
	"Turns off all LEDs in array of LED objects provided"
	print "\nSwitching off all LEDs!"
	for index in range(len(leds)):
		leds[index].stop()
	return

#function to update the pin duty cylces
def updateLeds( leds, duty_cycles ):
	"Updates all leds with latest duty cycle provided"
	print "\nUpdating LED duty cycles!"
	for index in range(len(leds)):
		leds[index].ChangeDutyCycle(duty_cycles[index])
	return

#welcome statements
print "\nCloud Clouds is starting..."

#setup GPIO output pins
print "\nSetting up GPIO pins and libraries..."
GPIO.setmode(GPIO.BCM)
#LED Strip 1
GPIO.setup(17, GPIO.OUT)	#LED Red 1
GPIO.setup(18, GPIO.OUT)	#LED Green 1
GPIO.setup(27, GPIO.OUT)	#LED Blue 1
#LED Strip 2w
GPIO.setup(23, GPIO.OUT)	#LED Red 2
GPIO.setup(24, GPIO.OUT)	#LED Green 2
GPIO.setup(25, GPIO.OUT)	#LED Blue 2
#LED Strip 3
GPIO.setup(10, GPIO.OUT)	#LED Red 3
GPIO.setup(9, GPIO.OUT)	#LED Green 3
GPIO.setup(11, GPIO.OUT)	#LED Blue 3

#create an array to store all the led objects
leds = []
#LED Strip 1
led = GPIO.PWM(17, LED_FREQ)
leds.append(led)
led = GPIO.PWM(18, LED_FREQ)
leds.append(led)
led = GPIO.PWM(27, LED_FREQ)
leds.append(led)
#LED strip 2
led = GPIO.PWM(23, LED_FREQ)
leds.append(led)
led = GPIO.PWM(24, LED_FREQ)
leds.append(led)
led = GPIO.PWM(25, LED_FREQ)
leds.append(led)
#LED strip 3
led = GPIO.PWM(10, LED_FREQ)
leds.append(led)
led = GPIO.PWM(9, LED_FREQ)
leds.append(led)
led = GPIO.PWM(11, LED_FREQ)
leds.append(led)

#create an array to store all the led pin duty cycles
duty_cycles = [1, 1, 1, 1, 1, 1, 1, 1, 1]

#start all the leds
startLeds(leds, duty_cycles)

#main program loop
#inifite, just updates the LED duty cycles from the duty_cycles array and drives them up and down
while (1):
	print "\nMain program loop started."

	#update the duty cycles from 0% to 100%
	for i in range(0, 100, 1):
		for j in range(len(duty_cycles)):
			duty_cycles[j] = i/100

		#send new duty cyles to LEDs
		updateLeds( leds, duty_cycles)

		#wait for some time for the changes to take effect
		time.sleep(0.1)

	#update the duty cycles from 100% to 0%
	for i in range(100, 0, -1):
		for j in range(len(duty_cycles)):
			duty_cycles[j] = i/100
			
		#send new duty cyles to LEDs
		updateLeds( leds, duty_cycles)

		#wait for some time for the changes to take effect
		time.sleep(0.1)