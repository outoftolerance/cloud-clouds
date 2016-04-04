########################### Functions ###########################
#################################################################

# Import libraries
import pywapi				# Weather API library
import pygame				# Pythong library for sound, keyboard entries, etc...
import time
import datetime				# Structure defined as datetime(Year, Month, Day, Hour, Minute Second, Millisecond)
import pigpio				# Pi GPIO library

#### Remove this once all functions have been transfered to this file
import controller
####

# Need to install - enter: pip install astral
from astral import Astral 	# Class with functions for calculating sunrise-sunset times

# Variable definitions
setLocation = "CAXX0518"		# Vancouver-Canada
setCity = "Vancouver"


##### Weather Class #####
# Input: Location, Units - default: metric
#########################
class CWeather:

	def _init_(self, setCity, setLocation, setUnits = "metric"):
		self.location = setLocation
		self.units = setUnits
		self.city = setCity
		weatherData = pywapi.get_weather_from_weather_com(self.location, units = self.units )
		astrology = Astral()
		sunLocation = astrology[self.city]

	def getCondition(self):
		conditionStatus = weatherData["current_conditions"]["text"]

		# 7 Catagories - returns a string: Cloud, Sun, Rain, Snow, Storm, Fog... default: Clear
		if conditionStatus == ("Cloudy" or "Partly Cloudy" or "Mostly Cloudy" or "Overcast"):
			return "Cloud"
		elif conditionStatus == ("Sunny" or "Partly Sunny" or "Mostly Sunny"):
			return "Sun"
		elif conditionStatus == ("Rain" or "Showers" or "Chance of Rain" or "Light Rain" or "Scattered Showers" or "Freezing Drizzle" or "Drizzle"):
			return "Rain"
		elif conditionStatus == ("Rain and Snow" or "Snow" or "Chance of Snow" or "Sleet" or "Icy" or "Snow Showers" or "Hail" or "Light Snow"):
			return "Snow"
		elif conditionStatus == ("Storm" or "Thunderstorm" or "Chance of Thunderstorm" or "Chance of Storm" or "Scattered Thunderstorms"):
			return "Storm"
		elif weatherStatus == ("Fog" or "Smoke" or "Dust" or "Haze" or "Mist"):
			return "Fog"
		else:
			#the default daytime setting
			return "Clear"

	def getTemperature(self):
		temperatureStatus = weatherData["current_conditions"]["temperature"]
		return float(temperatureStatus)		#Returns a float value - units: Celcius

	def getSunRiseTime(self):
		sunriseStatus = sunLocation.sun(date = datetime.date.today(), local = True)
		strSunrise = str(sunriseStatus["sunrise"])
		sunriseTime = strSunrise[11] + strSunrise[12] + strSunrise[13] + strSunrise[14] + strSunrise[15] + strSunrise[16] + strSunrise[17] + strSunrise[18]
		return sunriseTime 			#Returns a string - format: [HH:MM:SS] 24h clock


	def getSunSetTime(self):
		sunsetStatus = sunLocation.sun(date = datetime.date.today(), local = True)
		strSunset = str(sunsetStatus["sunset"])
		sunsetTime = strSunset[11] + strSunset[12] + strSunset[13] + strSunset[14] + strSunset[15] + strSunset[16] + strSunset[17] + strSunset[18]
		return sunsetTime 			#Returns a string - format: [HH:MM:SS] 24h clock

	def getWindSpeed(self):
		windSpeedStatus = weatherData["current_conditions"]["wind"]["speed"]
		return float(windSpeedStatus)		#Returns a float value - units: km/h

	def getVisibility(self):
		visibilityStatus =  weatherData["current_conditions"]["visibility"]
		return float(visibilityStatus)		#Returns float value - units: km
		



