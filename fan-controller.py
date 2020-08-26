#!/usr/bin/python

"""
Script to automatically turn the fan on the RPi on/off
based on CPU temperature thresholds
"""
from time import sleep
from gpiozero import OutputDevice, CPUTemperature

cpu_thermostat = CPUTemperature()
fan = OutputDevice(14, initial_value=False)

max_threshold = 50
min_threshold = 35

while True:
    temp = cpu_thermostat.temperature
    if temp >= max_threshold:
        fan.on()
    elif temp < min_threshold:
        fan.off()
    sleep(1)
