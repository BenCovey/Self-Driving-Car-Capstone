#!/usr/bin/python
import curses
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time
import atexit
# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)
# i = speed
i = 255
m1 = mh.getMotor(1)
m2 = mh.getMotor(2)
m3 = mh.getMotor(3)
m4 = mh.getMotor(4)
m1.setSpeed(i)
m2.setSpeed(i)
m3.setSpeed(i)
m4.setSpeed(i)
# recommended for auto-disabling motors on shutdown!


def turn_off_motors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)


def test_motors():
    # DC motor test!
    m1.run(Adafruit_MotorHAT.BACKWARD)
    m2.run(Adafruit_MotorHAT.FORWARD)
    m3.run(Adafruit_MotorHAT.BACKWARD)
    m4.run(Adafruit_MotorHAT.FORWARD)
    time.Sleep(.25)
    m1.run(Adafruit_MotorHAT.FORWARD)
    m2.run(Adafruit_MotorHAT.BACKWARD)
    m3.run(Adafruit_MotorHAT.FORWARD)
    m4.run(Adafruit_MotorHAT.BACKWARD)
    time.Sleep(.25)
    turn_off_motors()

def go_straight():
    i = 255
    m1.setSpeed(i)
    m2.setSpeed(i)
    m3.setSpeed(i)
    m4.setSpeed(i)
    m1.run(Adafruit_MotorHAT.BACKWARD)
    m2.run(Adafruit_MotorHAT.FORWARD)
    m3.run(Adafruit_MotorHAT.FORWARD)
    m4.run(Adafruit_MotorHAT.BACKWARD)


def turn_right():
    i = 124
    m1.setSpeed(i)
    m2.setSpeed(i)
    m3.setSpeed(i)
    m4.setSpeed(i)
    m1.run(Adafruit_MotorHAT.FORWARD)
    m2.run(Adafruit_MotorHAT.BACKWARD)
    m3.run(Adafruit_MotorHAT.FORWARD)
    m4.run(Adafruit_MotorHAT.BACKWARD)


def turn_left():
    i = 124
    m1.setSpeed(i)
    m2.setSpeed(i)
    m3.setSpeed(i)
    m4.setSpeed(i)
    m1.run(Adafruit_MotorHAT.BACKWARD)
    m2.run(Adafruit_MotorHAT.FORWARD)
    m3.run(Adafruit_MotorHAT.BACKWARD)
    m4.run(Adafruit_MotorHAT.FORWARD)

    
atexit.register(turn_off_motors())


stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr(0,10,"Hit 'q' to quit")
stdscr.refresh()

key = ''
while key != ord('q'):
    key = stdscr.getch()
    stdscr.addch(20,25,key)
    stdscr.refresh()
    if key == curses.KEY_UP:
        i = 255
        m1.setSpeed(i)
        m2.setSpeed(i)
        m3.setSpeed(i)
        m4.setSpeed(i)
        m1.run(Adafruit_MotorHAT.BACKWARD)
        m2.run(Adafruit_MotorHAT.FORWARD)
        m3.run(Adafruit_MotorHAT.FORWARD)
        m4.run(Adafruit_MotorHAT.BACKWARD)

        stdscr.addstr("Current mode: FORWARDS       ",curses.A_REVERSE)
        
    elif key == curses.KEY_DOWN:
        i = 255
        m1.setSpeed(i)
        m2.setSpeed(i)
        m3.setSpeed(i)
        m4.setSpeed(i)
        m1.run(Adafruit_MotorHAT.FORWARD)
        m2.run(Adafruit_MotorHAT.BACKWARD)
        m3.run(Adafruit_MotorHAT.BACKWARD)
        m4.run(Adafruit_MotorHAT.FORWARD)

        stdscr.addstr("Current mode: BACKWARDS      ",curses.A_REVERSE)
        
    elif key == curses.KEY_LEFT:
        i = 124
        m1.setSpeed(i)
        m2.setSpeed(i)
        m3.setSpeed(i)
        m4.setSpeed(i)
        m1.run(Adafruit_MotorHAT.BACKWARD)
        m2.run(Adafruit_MotorHAT.FORWARD)
        m3.run(Adafruit_MotorHAT.BACKWARD)
        m4.run(Adafruit_MotorHAT.FORWARD)
        stdscr.addstr("Current mode: TURNING LEFT    ",curses.A_REVERSE)

    elif key == curses.KEY_RIGHT:
        i = 124
        m1.setSpeed(i)
        m2.setSpeed(i)
        m3.setSpeed(i)
        m4.setSpeed(i)
        m1.run(Adafruit_MotorHAT.FORWARD)
        m2.run(Adafruit_MotorHAT.BACKWARD)
        m3.run(Adafruit_MotorHAT.FORWARD)
        m4.run(Adafruit_MotorHAT.BACKWARD)
        stdscr.addstr("Current mode: TURNING RIGHT   ",curses.A_REVERSE)

    else:
        turn_off_motors()
        stdscr.addstr("Current mode: STOPPING          ",curses.A_REVERSE)
curses.endwin()
