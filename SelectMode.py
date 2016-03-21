########################### Select Mode #########################
#################################################################
# Objective:	Based on mode, run script.

import time
import datetime	#Structure defined as datetime(Year, Month, Day, Hour, Minute Second, Millisecond)

mode = weatherMode # Have this in the main controller file - this is temp


# Mode 1 = Weather (Currently the only option)
while (mode == weatherMode):								#Infinite Loop
	currentTime = datetime.datetime.now()					#Define current time

	if currentTime.hour >= 6 and currentTime.hour <= 18:
		##### Run Day Mode - Enter Function #####
		print ("Day Mode")
	else:
		##### Run Night Mode - Enter Function Here #####
		print ("Night Mode")

	time.sleep(60000)										#Check hour every minute