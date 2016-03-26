########################### Functions ###########################
#################################################################


import pywapi

# Get user input for mode
def GetMode ():
	#Different Modes
	weatherMode = 1
	lampMode = 2
	partyMode = 3

	mode = raw_input("Select Mode Number: 1-Weather; 2-Lamp; 3-Party\n")

	return

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





