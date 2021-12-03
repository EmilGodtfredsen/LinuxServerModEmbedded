# Raspberry pi sensehat binary clock. Capable of doing 6 (horizontal) or 3 (vertical) column binary coded decimal (BCD) w/ 12- and 24-hour support.

optional arguments:
-h, --help          show this help message and exit
-o, --orientation {v, h}
                    Start up the clock in [v]ertical or [h]orizontal mode. Default is horizontal
-12, --twelve-hour-format
                    Use the 12 hour clock format instead of the default 24 hour one.

# Running program as a service
- Creating the service you need to copy the service file: cp binary_clock.service /lib/systemd/system/     binary_clock.service. Note that you need to change the ExecStart in the file to the path of your program. then reload the daemons with systemctl daemon-reload
- To enable the service: systemctl enable binary_clock.service
- To enable the service: systemctl disable binary_clock.service
- To run the service: systemctl start binary_clock.service
- To stop the service: systemctl stop binary_clock.service

# Change orientation with sense hat joystick
- Right for horizontal
- Left for vertical

# Change the clock hour format between 12-hour or 24-hour
- Up for 12-hour format 
- Down for 24-hour (military) format