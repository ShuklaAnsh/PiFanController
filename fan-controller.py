#!/usr/bin/python

"""
Script to automatically turn the fan on the RPi on/off
based on CPU temperature thresholds
"""
from time import sleep
from gpiozero import OutputDevice, CPUTemperature

gpio_pin_bcm = 23
cpu_thermostat = CPUTemperature()
fan = OutputDevice(gpio_pin_bcm, initial_value=False)

max_threshold = 60
min_threshold = 40

while True:
    temp = cpu_thermostat.temperature
    if temp >= max_threshold:
        fan.on()
    elif temp < min_threshold:
        fan.off()
    sleep(1)
