# Rasberry Pi Screenwake

I started a project to use my Pi 3b+ as a digital calendar for the family. But I didn't want the screen on AAAAAAALLLL the time and I needed a way to wake my Raspberry Pi 3b+ screen when it went to sleep. After a lot of searching, I came across these 2 videos:

"How to Add a Power Button to Your Raspberry Pi (+ FLIRC Case Install!)" - Howchoo
https://www.youtube.com/watch?v=wVnMZ4DXDNo

"How to Turn a Raspberry Pi Display Off & On Using a Python Script, + How to Disable the ScreenSaver" - BaldGuyDIY
https://www.youtube.com/watch?v=lETqSCimcyM

After watching Bald Guy DIY, I was able to use his notes to modify Howchoo's scripts. And to be able to make it easier to load using Howchoo's instructions, 
I have basiaclly copied his entire repository (https://github.com/Howchoo/pi-power-button) and modified the install and uninstall to match my new scripts.

This script that I am using wires to the GPIO header.  Specifically GPIO 14 (physical pin 8) and GND (physical pin 6).

I may take this and work on it a little more and see if I can add a time based trigger to shut off the screen at a certain time at night, and then wake up in the morning automatically when we start our day.
