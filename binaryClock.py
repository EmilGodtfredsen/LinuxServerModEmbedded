#!/usr/bin/env python

from sense_hat import SenseHat

import time, datetime
import pytz
import signal
hat = SenseHat()
vertical = True
mili_clock = True
should_exit = False
color = (0, 230, 0)
russia = pytz.timezone('Asia/Vladivostok')
off = (0, 0, 0)

hat.clear()
def display_binary_horizontal(y, value):
    binary_str = "{0:8b}".format(value) 
    for x in range(0, 8):
        if binary_str[x] == '1':
            hat.set_pixel(x, y, color)
        else:
            hat.set_pixel(x, y, off)

def display_binary_vertical(x, value):
    binary_str = "{0:8b}".format(value)
    for y in range(0, 8):
        if binary_str[y] == '1':
            hat.set_pixel(x, y, color)
        else:
            hat.set_pixel(x, y, off)

def set_orientation(event):
    global vertical, mili_clock
    if event.direction == 'right':
        hat.clear()
        vertical = False
    elif event.direction == 'left':
        hat.clear()
        vertical = True
    if event.direction == 'up':
        hat.clear()
        mili_clock = False
    else:
        hat.clear()
        mili_clock = True
hat.stick.direction_any = set_orientation


def before_exit(Signum, frame):
    hat.show_message("Programmet slutter", 0.01)
    global should_exit
    should_exit = True
    

signal.signal(signal.SIGINT, before_exit)
signal.signal(signal.SIGTERM, before_exit)

def main():
    hat.show_message("Programmet starter", 0.01)  
    while not should_exit:
        t = datetime.datetime.now(russia)
        if mili_clock:
            time_now = t.strftime('%H%M%S')
        else:
            time_now = t.strftime('%I%M%S')

        if vertical:
            time_now = [int(i) for i in time_now]
            time_now = [0, time_now[0]] if len(time_now) == 1 else time_now      
            for i in range(6):
                display_binary_vertical(i, time_now[i])
        else:
            time_now = [int(time_now[i:i+2]) for i in range(0, len(time_now), 2)]
            time_now = [0, time_now[0]] if len(time_now) == 1 else time_now 
            for i in range(3):
                display_binary_horizontal(i, time_now[i])
        time.sleep(0.0001)
    hat.clear()     

if __name__ == "__main__": 
    main()
