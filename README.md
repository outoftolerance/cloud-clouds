# Cloud Clouds

Cloud Clouds is a project designed to create indoor cloud like lighting which can mimic realistic outdoor weather patterns using LED lighting and a variety of sound effects. The core of the project is the Raspberry Pi embedded computer, which manages the lighting effects, sound effects, communications with online weather APIs, and much more. This repository stores the code required to enable these features.

> The overriding design goal for this project was to create an IoT connected object which would bring a bit of nature indoors, creating a better living and work environment for inhabitants of the space, and enable them to connect with the environment in a technologically interresting way. (Additionally it meets the criteria for the final project of MECH 423 at the university of British Columbia!)

See more about the project and how you can make it at James' website: [Out Of Tolerance](https://www.outoftolerance.com/projects "Out Of Tolerance")

### Installation
Install the latest Raspbian image onto the Raspberry Pi's SD card and make sure your software is fully up to date by running the following.

    sudo apt-get update 
    sudo apt-get upgrade

Clone the Cloud Clouds repo into the Documents folder on the Raspberry Pi as follows.

    cd ~/Documents
    git clone https://www.github.com/outoftolerance/cloud-clouds
    
Install the required libraries by executing the following lines of code in the terminal.

    cd ~/Documents/cloud-clouds/RPi.GPIO-0.6.2
    python setup.py
    
Run the Cloud Clouds controller as follows.

    cd ~/Documents/cloud-clouds
    python controller.py

### Special Thanks

Cloud Clouds uses a number of open source libraries including the following. Please give them the respect they deserve and the thanks for all the hard work they have put in to enable the quick and easy development of our application!

- [RPi GPIO](https://sourceforge.net/projects/raspberry-gpio-python/) - A Raspberry Pi GPIO library for python

### Todos
 - Add night mode
 - Add day mode
 - Add integration with weather APIs
 - Add web configuration interface
 - Add sound effects for weather (wind, rain, hail, snow, thunderstorm, etc)
 - Test lighting effects with LED control board
 - Add transitional periods (sunrise, sunset, etc)
 - Add seasonal sound effects (day different in summer vs winter, etc)

License
----

MIT - See licence file in repo
