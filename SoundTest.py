# Sound Test File - Plays 2 sounds, one after the other
from pygame import mixer


while (1):
	mixer.init()
	mixer.music.load("/home/pi/Documents/cloud-clouds/Sounds/Wind1.mp3")
	while mixer.music.get_busy() == True:
		continue

	mixer.music.load("/home/pi/Documents/cloud-clouds/Sounds/Cricket1.mp3")
	while mixer.music.get_busy() == True:
		continue
