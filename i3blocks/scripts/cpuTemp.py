#! /usr/bin/python
from gpiozero import CPUTemperature 

cpu = CPUTemperature()

print(' ' + str(round(cpu.temperature)) + 'C')

