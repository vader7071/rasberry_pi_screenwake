#!/usr/bin/env python


import RPi.GPIO as GPIO
import subprocess

# setup GPIO pin - Using GPIO pin 14 (physical pin 8)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.wait_for_edge(14, GPIO.FALLING)

from subprocess import run
run('vcgencmd display_power 1', shell=False)

##### Time Delay to turn screen off #####
# import time
#
# counter = 300 # 5 minutes
# start = time.time()
# while True:
#    time.sleep(0.1)
#
#    if time.time() - start > 1:
#        start = time.time()
#        counter = counter - 1
#
#        if counter <= 0:
#            run('vcgencmd display_power 0', shell=False)
#            break
#########################################

# from "Howchoo"
# subprocess.call(['shutdown', '-h', 'now'], shell=False)

# from "Bald Guy DIY"
# run('vcgencmd display_power 0', shell=True)
