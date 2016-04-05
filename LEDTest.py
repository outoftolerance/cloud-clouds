# LED Color Test File - check to see all LEDs are functioning
# Make sure to load following: sudo pigpiod

import pigpio
import time

BRIGHTNESS = 0
EMPTY = 0

pi = pigpio.pi()

# Pulse the LEDs, each strip solid color of RED, GREEN, BLUE
while (1):
	while (BRIGHTNESS < 245.0):
		BRIGHTNESS = BRIGHTNESS + 1
		#display RED
		pi.set_PWM_dutycycle(17,BRIGHTNESS)
		pi.set_PWM_dutycycle(18,EMPTY)
		pi.set_PWM_dutycycle(27,EMPTY)
		#display GREEN
		pi.set_PWM_dutycycle(23,EMPTY)
		pi.set_PWM_dutycycle(24,BRIGHTNESS)
		pi.set_PWM_dutycycle(25,EMPTY)
		#display BLUE
		pi.set_PWM_dutycycle(10,EMPTY)
		pi.set_PWM_dutycycle(9,EMPTY)
		pi.set_PWM_dutycycle(11,BRIGHTNESS)
		time.sleep(0.01)

	while (BRIGHTNESS > 5.0):
		BRIGHTNESS = BRIGHTNESS - 1
		#display RED
		pi.set_PWM_dutycycle(17,BRIGHTNESS)
		pi.set_PWM_dutycycle(18,EMPTY)
		pi.set_PWM_dutycycle(27,EMPTY)
		#display GREEN
		pi.set_PWM_dutycycle(23,EMPTY)
		pi.set_PWM_dutycycle(24,BRIGHTNESS)
		pi.set_PWM_dutycycle(25,EMPTY)
		#display BLUE
		pi.set_PWM_dutycycle(10,EMPTY)
		pi.set_PWM_dutycycle(9,EMPTY)
		pi.set_PWM_dutycycle(11,BRIGHTNESS)
		time.sleep(0.01)
