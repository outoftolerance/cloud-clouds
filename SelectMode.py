########################### Select Mode #########################
#################################################################
# Objective:	Based on mode, run script.

import time
import datetime			# Structure defined as datetime(Year, Month, Day, Hour, Minute Second, Millisecond)
import DayMode			# Defines function RunWeatherStatus( location )

location = "CAXX0518"	# Vancouver-Canada


GetMode()

# Mode 1 = Weather (Currently the only option)
while (mode == weatherMode):								#Infinite Loop
	currentTime = datetime.datetime.now()					#Define current time

	if currentTime.hour > 6 and currentTime.hour < 18:
		RunWeatherStatus( location )
		print ("Day Mode")
	elif currentTime.hour == 18 and currentTime.minute == 0:
		##### Run night transition loop lasting 1 minute #####
		print ("Night Transition")
	elif currentTime.hour == 6 and currentTime.minute == 0:
		##### Run day transition loop lasting 1 minute #####
		print ("Day Transition")
	else:
		##### Run Night Mode - Enter Function Here #####
		print ("Night Mode")

	time.sleep(60)											#Check hour every minute

