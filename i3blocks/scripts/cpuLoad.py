#! /usr/bin/python

import psutil as p 

cpuPercent = p.cpu_percent(interval=1)
cpuChar = ''

print('{} {}%'.format(cpuChar, cpuPercent))

