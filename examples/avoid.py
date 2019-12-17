#!/usr/bin/env python
'''
**********************************************************************
* Filename    : ultra_sonic_avoidance.py
* Description : An example for sensor car kit to followe light
* Author      : Dream
* Brand       : SunFounder
* E-mail      : service@sunfounder.com
* Website     : www.sunfounder.com
* Update      : Dream    2016-09-27    New release
**********************************************************************
'''

from SunFounder_Ultrasonic_Avoidance import Ultrasonic_Avoidance
from source.car import Wheels, Car, Direction, Speed
import picar

picar.setup()

sensor = Ultrasonic_Avoidance.Ultrasonic_Avoidance(20)
wheels = Wheels()
print("Turning offset %d"%wheels.front._turning_offset)
speed = Speed()
pcar = Car(wheels = wheels, speed = speed, sensor = sensor)
direction = Direction(pcar)
pcar.dir = direction

try:
    pcar.avoidance()
except KeyboardInterrupt:
    pcar.stop()

