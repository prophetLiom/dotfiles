#!/usr/bin/python
#
# netStats.py
# gets them net stats so we can see in the bar

import sys
import subprocess

interface = "wlan0"

upDown = subprocess.call(['grep wlan0 ~/home/pi/proc/net/wireless | awk "{ print int($3 * 100 / 70)  }"'])


print(upDown)
