#!/usr/bin/env python

from sense_hat import SenseHat

import time, datetime

hat = SenseHat()

color = (0, 255, 0)

off = (0, 0, 0)

hat.clear()

def display_binary_horizontal(value, row, color):
    binary_str = "{0:8b}".format(value)
    for x in range(0, 8):
        if binary_str[x] == '1':
            hat.set_pixel(x, row, color)
        else:
            hat.set_pixel(x, row, off)

def display_binary_vertical(col, value, color):
    binary_str = "{0:8b}".format(value)
    for y in range(0, 8):
        if binary_str[y] == '1':
            hat.set_pixel(col, y, color)
        else:
            hat.set_pixel(col, y, off)

while True:
    t = datetime.datetime.now()
    time_now = t.strftime('%H%M%S')
    for event in hat.stick.get_events():
        print(event.direction, event.action)
    time_now = [int(i) for i in time_now]
    time_now = [0, time_now[0]] if len(time_now) == 1 else time_now      
    for i in range(6):
        display_binary_vertical(i, time_now[i], color)
    #display_binary_horizontal(t.hour, 5, hour_color)
    #display_binary_horizontal(t.minute, 6, minute_color)
    #display_binary_horizontal(t.second, 7, second_color)
    time.sleep(0.0001)