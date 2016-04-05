#!/usr/bin/env python2
#import all the libraries and elements that we need
import time
import sys
import pigpio
import string
#import CloudFunctions

#setup a pi object
pi = pigpio.pi()

#define global variables defaults
LOCATION = "CAXX0518"	#location of the weather we want
UNITS = "metric"	#default units for the weather
MODE = "lamp"	#mode we want to be in (default is mirror weather at location)
DEFAULT_COLOR = [255, 255, 255]	#default colour shown in lamp and pulse mode
WEATHER = ["Clear",26,0700,1900,15]	#default weather, clear, 26 degrees, sunrise 7am, 7pm sunset, 15km/h winds
COUNT = 0
DIRECTION = 1

#setup a location object for weather
#location = CWeather(LOCATION, UNITS)

#get the latest weather from location
#WEATHER = location.getStatus()

#open the settings file and grab all our globals from there
config = open("settings.conf", "r")
line = config.readline()
print "Line Read: %s" % (line)
line = config.readline()
print "Line Read: %s" % (line)
line = config.readline()
print "Line Read: %s" % (line)

with open("settings.conf", "r") as f:
    for line in f:
    	setting = string.split(line, "=")
        if setting[0] == "location":
        	LOCATION = setting[1]
        elif setting[0] == "units":
        	UNITS = setting[1]
        elif setting[0] == "mode":
        	MODE = setting[1]
        elif setting[0] == "colour":
        	DEFAULT_COLOR = string.split(setting[1], ",")
        else:
        	print "\nSetting in config file not recognised %s" % line

#close the file for other programs
f.close()

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
	for channel in range(0, 9, 3):
		for colour in range (0, 3, 1):
			duty_cycles[channel + colour] = DEFAULT_COLOR[colour]
	return

#function for pulsing mode
def pulseMode(cycle, previous_duty_cycles, duty_cycles, DEFAULT_COLOR):
	"Pulses a given colour"
	for channel in range(0, 9, 3):
		for colour in range (0, 3, 1):
			duty_cycles[channel + colour] = (cycle[COUNT] / 100) * DEFAULT_COLOR[colour]

	#check the limits and swap dir if needed
	if cycle[COUNT] >= 100 or cycle[COUNT] <= 0:
		if cycle[DIRECTION] == 1:
			cycle[DIRECTION] = 0
		else:
			cycle[DIRECTION] = 1

	#increment/decrement the counter based on direction
	if cycle[DIRECTION] == 1:
		cycle[COUNT] = cycle[COUNT] + 1
	else:
		cycle[COUNT] = cycle[COUNT] - 1



#function which runs the duty cycles for weather mode
def weatherMirrorMode(cycle, previous_duty_cycles, duty_cycles, WEATHER):
	"Outputs duty cycle values based on weather outside"
	#get the latest weather from the weather object
	#WEATHER = weather.getStatus()

	#set the LED colour based on conditions
		#check if it's sunrise
		#check if it's sunset
		

	#set the sound based on conditions

	return

#function which runs the duty cycles for weather mode inverted
def weatherInvertMode(cycle, previous_duty_cycles, duty_cycles, WEATHER):
	"Outputs duty cycle values based on weather outside inverted"
	return

#welcome statements
print "\nCloud Clouds is starting..."

#setup GPIO output pins
print "\nSetting up GPIO pins and libraries..."
leds = [17, 18, 27, 23, 24, 25, 10, 9, 11]
duty_cycles = [0, 0, 0, 0, 0, 0, 0, 0, 0]
previous_duty_cycles = [0, 0, 0, 0, 0, 0, 0, 0, 0]
cycle = [0, 1];

#start all the leds
startLeds(leds, duty_cycles)

#main program loop
#inifite, just updates the LED duty cycles from the duty_cycles array and drives them up and down
while (1):
	print "\nMain program loop started."

	#check what mode we are in and run appropriate function
	if MODE == "mirror":
		print "\nGetting latest from weather mirror mode"
		mirrorWeatherMode(cycle, previous_duty_cycles, duty_cycles, WEATHER)
	elif MODE == "invert":
		print "\nGetting latest from weather invert mode"
		invertWeatherMode(cycle, previous_duty_cycles, duty_cycles, WEATHER)
	elif MODE == "pulse":
		print "\nGetting latest from weather invert mode"
		pulseMode(cycle, previous_duty_cycles, duty_cycles)
	else:
		print "\nGetting latest from lamp mode"
		lampMode(duty_cycles, DEFAULT_COLOR)

	#update the LED duty cycles
	print "\nUpdating LED duty cycles."
	updateLeds(leds, duty_cycles)