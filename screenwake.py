#!/usr/bin/env python


import RPi.GPIO as GPIO
import subprocess

# setup GPIO pin - Using GPIO pin 14 (physical pin 8)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.wait_for_edge(14, GPIO.FALLING)

run('vcgencmd display_power 1', shell=True)

# subprocess.call(['shutdown', '-h', 'now'], shell=False)

# from subprocess import run
# run('vcgencmd display_power 0', shell=True)
