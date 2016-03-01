#!/usr/bin/env python2
#import all the libraries and elements that we need
import time
import sys
import RPi.GPIO as GPIO

#define global variables
LED_FREQ = 1000	#frequency of LED PWM switching

#welcome statements
print "\nCloud Clouds is starting..."

#setup GPIO output pins
print "\nSetting up GPIO pins and libraries..."
GPIO.setmode(GPIO.BOARD)
GPIO.setup(0, GPIO.OUT)	#LED Red 1
GPIO.setup(1, GPIO.OUT)	#LED Green 1
GPIO.setup(2, GPIO.OUT)	#LED Blue 1


#create an array to store all the led objects
leds = []
led = GPIO.PWM(0, LED_FREQ)
leds.append(led)
led = GPIO.PWM(1, LED_FREQ)
leds.append(led)
led = GPIO.PWM(2, LED_FREQ)
leds.append(led)

#create an array to store all the led pin duty cycles
duty_cycles = [1, 1, 1, 1, 1, 1, 1, 1, 1]

#start all the leds
startLeds(leds, duty_cycles)

#main program loop
while (1):
	print "\nMain program loop started."
	updateLeds( leds, duty_cycles)

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
