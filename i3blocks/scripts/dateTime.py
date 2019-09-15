#! /usr/bin/python

import datetime

now = datetime.datetime.now()

print(' ' + now.strftime("%a %b %-d") + '  ' + now.strftime("%-I:%M%p  "))

