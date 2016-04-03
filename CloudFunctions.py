########################### Functions ###########################
#################################################################

# Import libraries
import pywapi		# Weather API library
import pygame		# Pythong library for sound, keyboard entries, etc...
import time
import datetime		# Structure defined as datetime(Year, Month, Day, Hour, Minute Second, Millisecond)
import pigpio		# Pi GPIO library
import controller

# Variable definitions
location = "CAXX0518"	# Vancouver-Canada

def DefineGPIOPins():
	redLED1 = 17
	greenLED1 = 18
	blueLED1 = 27
	redLED2 = 23
	greenLED2 = 24
	blueLED2 = 25
	redLED3 = 10
	greenLED3 = 9
	blueLED3 = 11


# Get user input for mode
def GetMode ():
	#Different Modes
	weatherMode = 1
	lampMode = 2
	partyMode = 3

	mode = raw_input("Select Mode Number: 1-Weather; 2-Lamp; 3-Party\n")

	return


class CWeather:

	def _init_(self, setLocation, setUnits = "metric"):
		self.setLocation = setLocation
		self.setUnits = setUnits
		weatherData = pywapi.get_weather_from_weather_com(self.setLocation, units = self.setUnits )

	def getCondition(self):
		conditionStatus = weatherData["current_conditions"]["text"]

		if conditionStatus == ("Cloudy" or "Partly Cloudy" or "Mostly Cloudy" or "Overcast"):
			print("Cloud")
			return statusCloud
		elif conditionStatus == ("Sunny" or "Partly Sunny" or "Mostly Sunny"):
			#LED setting for Sunny
			print("Sun")
			return statusSun
		elif conditionStatus == ("Rain" or "Showers" or "Chance of Rain" or "Light Rain" or "Scattered Showers" or "Freezing Drizzle" or "Drizzle"):
			#LED setting for Rain
			print("Rain")
			return statusRain
		elif conditionStatus == ("Rain and Snow" or "Snow" or "Chance of Snow" or "Sleet" or "Icy" or "Snow Showers" or "Hail" or "Light Snow"):
			#LED setting for Snow
			print("Snow")
			return statusSnow
		elif conditionStatus == ("Storm" or "Thunderstorm" or "Chance of Thunderstorm" or "Chance of Storm" or "Scattered Thunderstorms"):
			#LED setting for Storm
			print("Storm")
			return statusStorm
		elif weatherStatus == ("Fog" or "Smoke" or "Dust" or "Haze" or "Mist"):
			#LED setting for Fog
			print("Fog")
			return statusFog
		else:
			#LED setting for Clear - the default daytime setting
			print("Clear")
			return statusClear

	def getTemperature(self):
		temperatureStatus = weatherData["current_conditions"]["temperature"]
		return float(temperatureStatus)

	def getSunRiseTime(self):
		sunriseStatus = weatherData["current_conditions"]["temperature"]

	def getSunSetTime(self):


	def getWindSpeed(self):
		#write something here




# Update weather data
def RunWeatherStatus( location ):
	weatherResult = pywapi.get_weather_from_weather_com(location, units = "metric" )
	weatherStatus = weatherResult["current_conditions"]["text"]

	if weatherStatus == ("Cloudy" or "Partly Cloudy" or "Mostly Cloudy" or "Overcast"):
		#LED setting for Cloudy
		print("Cloud")
	elif weatherStatus == ("Sunny" or "Partly Sunny" or "Mostly Sunny"):
		#LED setting for Sunny
		print("Sun")
	elif weatherStatus == ("Rain" or "Showers" or "Chance of Rain" or "Light Rain" or "Scattered Showers" or "Freezing Drizzle" or "Drizzle"):
		#LED setting for Rain
		print("Rain")
	elif weatherStatus == ("Rain and Snow" or "Snow" or "Chance of Snow" or "Sleet" or "Icy" or "Snow Showers" or "Hail" or "Light Snow"):
		#LED setting for Snow
		print("Snow")
	elif weatherStatus == ("Storm" or "Thunderstorm" or "Chance of Thunderstorm" or "Chance of Storm" or "Scattered Thunderstorms"):
		#LED setting for Storm
		print("Storm")
	elif weatherStatus == ("Fog" or "Smoke" or "Dust" or "Haze" or "Mist"):
		#LED setting for Fog
		print("Fog")
	else:
		#LED setting for Clear - the default daytime setting
		print("Clear")

	return


