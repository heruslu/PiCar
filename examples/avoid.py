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
#from picar import front_wheels
#from picar import back_wheels
from source.car import Wheels, Car, Direction, Speed
import time
import picar

picar.setup()

ua = Ultrasonic_Avoidance.Ultrasonic_Avoidance(20)
wheels = Wheels()
speed = Speed()
pcar = Car(wheels = wheels, speed = speed)
pcar.wheels.front.turning_max = 45
direction = Direction(pcar)
pcar.dir = direction

forward_speed = 100
backward_speed = 70

back_distance = 30
turn_distance = 40

timeout = 10

def start_avoidance():
    print('start_avoidance')

    count = 0
    while True:
        distance = ua.get_distance()
        print("distance: %scm" % distance)
        if distance > 0:
            count = 0
            if distance < back_distance: # backward
                pcar.backward()
            elif distance < turn_distance: # turn
                pcar.random_turn()
#                print("turn")
#                pcar.wheels.front.turn(pcar.dir.random_dir())
#                pcar.wheels.back.forward()
#                pcar.wheels.back.speed = forward_speed
#                time.sleep(1)
            else:
                pcar.forward()
#                pcar.wheels.front.turn_straight()
#                pcar.wheels.back.forward()
#                pcar.wheels.back.speed = forward_speed

        else:						# forward
            print('negative distance counter: %d'%count)
            pcar.wheels.front.turn_straight()
            if count > timeout:  # timeout, stop;
                pcar.wheels.back.stop()
            else:
                pcar.wheels.back.backward()
                pcar.wheels.back.speed = forward_speed
                count += 1

def stop():
    pcar.wheels.back.stop()
    pcar.wheels.front.turn_straight()

if __name__ == '__main__':
    try:
        start_avoidance()
    except KeyboardInterrupt:
        stop()
