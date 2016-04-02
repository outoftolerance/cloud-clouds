#!/usr/bin/env python2
#import all the libraries and elements that we need
import time
import sys
import pigpio
#import CloudFunctions

#setup a pi object
pi = pigpio.pi()

#define global variables defaults
LED_FREQ = 120	#frequency of LED PWM switching
LOCATION = "CAXX0518"	#location of the weather we want
MODE = "lamp"	#mode we want to be in (default is mirror weather at location)
DEFAULT_COLOR = [255, 255, 255]	#default colour shown in lamp mode

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
		pi.set_PWM_dutycycle(leds[index], duty_cycles[index])
	return

#function to stop all pins
def stopLeds( leds ):
	"Turns off all LEDs in array of LED objects provided"
	print "\nSwitching off all LEDs!"
	for index in range(len(leds)):
		pi.set_PWM_dutycycle(leds[index], 0)
		pi.stop()
	return

#function to update the pin duty cylces
def updateLeds( leds, duty_cycles ):
	"Updates all leds with latest duty cycle provided"
	print "\nUpdating LED duty cycles!"
	for index in range(len(leds)):
		real_brightness = int(int(duty_cycles[index]) * (float(255) / 255.0))
		pi.set_PWM_dutycycle(leds[index], real_brightness)
	return

#function to define lamp mode
def lampMode(duty_cycles, DEFAULT_COLOR):
	"Outputs duty cycle values based on lamp mode and default colour"
	for channel in range(0, 6, 3):
		for colour in range (0, 2, 1):
			duty_cycles[channel + colour] = DEFAULT_COLOR[colour]
			print "\nupdating pin"
			print (channel+colour)
	return

#function for pulsing mode
def pulseMode(duty_cycles, DEFAULT_COLOR):
	#update the duty cycles from 0% to 100%
	for i in range(0, 255, 1):
		for j in range(len(duty_cycles)):
			duty_cycles[j] = i

		#wait for some time for the changes to take effect
		time.sleep(0.01)

	#update the duty cycles from 100% to 0%
	for i in range(255, 0, -1):
		for j in range(len(duty_cycles)):
			duty_cycles[j] = i

		#wait for some time for the changes to take effect
		time.sleep(0.01)
	return

#function which runs the duty cycles for weather mode
def weatherMirrorMode(duty_cycles):
	"Outputs duty cycle values based on weather outside"
	return

#function which runs the duty cycles for weather mode inverted
def weatherMirrorMode(duty_cycles):
	"Outputs duty cycle values based on weather outside inverted"
	return

#welcome statements
print "\nCloud Clouds is starting..."

#setup GPIO output pins
print "\nSetting up GPIO pins and libraries..."
leds = [17, 18, 27, 23, 24, 25, 10, 9, 11]
duty_cycles = [0, 0, 0, 0, 0, 0, 0, 0, 0]

#start all the leds
startLeds(leds, duty_cycles)

#main program loop
#inifite, just updates the LED duty cycles from the duty_cycles array and drives them up and down
while (1):
	print "\nMain program loop started."

	#check what mode we are in and run appropriate function
	if MODE == "mirror":
		print "\nGetting latest from weather mirror mode"
		mirrorWeatherMode(duty_cycles)
	elif MODE == "invert":
		print "\nGetting latest from weather invert mode"
		invertWeatherMode(duty_cycles)
	elif MODE == "pulse":
		print "\nGetting latest from weather invert mode"
		pulseMode(duty_cycles)
	else:
		print "\nGetting latest from lamp mode"
		lampMode(duty_cycles, DEFAULT_COLOR)

	#update the LED duty cycles
	print "\nUpdating LED duty cycles."
	updateLeds(leds, duty_cycles)