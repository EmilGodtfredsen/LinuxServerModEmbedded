#!/usr/bin/env python

from sense_hat import SenseHat

import time, datetime
from pytz import timezone
from itertools import zip_longest

hat = SenseHat()

hour_color = (0, 255, 0)
minute_color = (0, 0, 255)
second_color = (255, 0, 0)
off = (0, 0, 0)

hat.clear()
england = timezone('Europe/Copenhagen')
def main():
    return(vertical_strings(bcd(Now)))

def display_binary_horizontal(value, row, color):
    binary_str = "{0:8b}".format(value)
    for x in range(0, 8):
        if binary_str[x] == '1':
            hat.set_pixel(x, row, color)
        else:
            hat.set_pixel(x, row, off)
def bcd(digits):
    'Convert a string of decimal digits to binary-coded-decimal.'
    def bcdigit(d):
        'Convert a decimal digit to BCD (4 bits wide).'
        # [2:] strips the '0b' prefix added by bin().
        return bin(d)[2:].rjust(4, '0')
    return (bcdigit(int(d)) for d in digits)

# vertical_strings :: iterable(str) -> str
def vertical_strings(strings):
    'Orient an iterable of strings vertically: one string per column.'
    iters = [iter(s) for s in strings]
    concat = ''.join
    return '\n'.join(map(concat,
                         zip_longest(*iters, fillvalue=' ')))
def set_hours():
    for i in range(4,12,2):
        if int(list(reversed(Time.split()))[i/2 - 2][0]) == 1:
            hat.set_pixel(2,i,240,40,100)
            hat.set_pixel(3,i,240,40,100)
            hat.set_pixel(2,i+1,240,40,100)
            hat.set_pixel(3,i+1,240,40,100)
        else:
            hat.set_pixel(2,i,0,0,0)
            hat.set_pixel(3,i,0,0,0)
            hat.set_pixel(2,i+1,0,0,0)
            hat.set_pixel(3,i+1,0,0,0)

    for i in range(4,12,2):
        if int(list(reversed(Time.split()))[i/2 - 2][1]) == 1:
            hat.set_pixel(4,i,240,40,100)
            hat.set_pixel(5,i,240,40,100)
            hat.set_pixel(4,i+1,240,40,100)
            hat.set_pixel(5,i+1,240,40,100)
        else:
            hat.set_pixel(4,i,0,0,0)
            hat.set_pixel(5,i,0,0,0)
            hat.set_pixel(4,i+1,0,0,0)
            hat.set_pixel(5,i+1,0,0,0)

def set_mins():
    for i in range(4,12,2):
        if int(list(reversed(Time.split()))[i/2 - 2][2]) == 1:
            hat.set_pixel(6,i,40,240,130)
            hat.set_pixel(7,i,40,240,130)
            hat.set_pixel(6,i+1,40,240,130)
            hat.set_pixel(7,i+1,40,240,130)
        else:
            hat.set_pixel(6,i,0,0,0)
            hat.set_pixel(7,i,0,0,0)
            hat.set_pixel(6,i+1,0,0,0)
            hat.set_pixel(7,i+1,0,0,0)

    for i in range(4,12,2):
        if int(list(reversed(Time.split()))[i/2 - 2][3]) == 1:
            hat.set_pixel(8,i,40,240,130)
            hat.set_pixel(9,i,40,240,130)
            hat.set_pixel(8,i+1,40,240,130)
            hat.set_pixel(9,i+1,40,240,130)
        else:
            hat.set_pixel(8,i,0,0,0)
            hat.set_pixel(9,i,0,0,0)
            hat.set_pixel(8,i+1,0,0,0)
            hat.set_pixel(9,i+1,0,0,0)

def set_secs():
    for i in range(4,12,2):
        if int(list(reversed(Time.split()))[i/2 - 2][4]) == 1:
            hat.set_pixel(10,i,40,90,255)
            hat.set_pixel(11,i,40,90,255)
            hat.set_pixel(10,i+1,40,90,255)
            hat.set_pixel(11,i+1,40,90,255)
        else:
            hat.set_pixel(10,i,0,0,0)
            hat.set_pixel(11,i,0,0,0)
            hat.set_pixel(10,i+1,0,0,0)
            hat.set_pixel(11,i+1,0,0,0)

    for i in range(4,12,2):
        if int(list(reversed(Time.split()))[i/2 - 2][5]) == 1:
            hat.set_pixel(12,i,40,90,255)
            hat.set_pixel(13,i,40,90,255)
            hat.set_pixel(12,i+1,40,90,255)
            hat.set_pixel(13,i+1,40,90,255)
        else:
            hat.set_pixel(12,i,0,0,0)
            hat.set_pixel(13,i,0,0,0)
            hat.set_pixel(12,i+1,0,0,0)
            hat.set_pixel(13,i+1,0,0,0)

def set_time():
    set_hours()
    set_mins()
    set_secs()

while True:
    t = datetime.datetime.now()
    Now = datetime.now(england).strftime('%H%M%S')
    Time = main()
    set_time()
    display_binary_horizontal(t.hour, 1, hour_color)
    display_binary_horizontal(t.minute, 2, minute_color)
    display_binary_horizontal(t.second, 3, second_color)
    time.sleep(0.0001)