# Tunerboard
Interface for controlling a tunerboard for a WFM repeater

Located in the south of the Netherlands, a manned Wide-FM repeater is in operation with (at the moment) 8 inputs on 70cm.
All inputs are able to receive 280KHz wide FM broadband stereo audio (with RDS).

Each tunerboard contain 4 tuners (XD-6686AF, available through AliExpress for only a few dollars) and are controlled
by an Arduino-alike microcontroller-board. Serial-port traffic is fed to an Raspberry-Pi which runs the python script
available from this project.

The generated JSON data is used to display a web page with status information (Work in Progress).

Changing of parameters is done remotely by feeding the Raspberry Pi commands through the COM2TCP functionality of the
python script. It basically allows remote access to serial (USB) ports of the Raspberry.

More info will be available (in the future) here: http://www.-het-bar.net
