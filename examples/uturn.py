#!/usr/bin/env python
from SunFounder_Ultrasonic_Avoidance import Ultrasonic_Avoidance
from source.car import Wheels, Car, Direction, Speed
import picar
import time

picar.setup()

sensor = Ultrasonic_Avoidance.Ultrasonic_Avoidance(20)
wheels = Wheels(turning_max = 45)
print("Turning offset %d"%wheels.front._turning_offset)
forward_speed = 60
backward_speed = 100
turn_duration = 220.0 / forward_speed
backward_turn_duration = 290.0 / backward_speed
speed = Speed(forward = forward_speed, backward = backward_speed)
pcar = Car(wheels = wheels, speed = speed, sensor = sensor)
direction = Direction(pcar,force_turning = 1)
pcar.dir = direction

try:
    print('forward')
    pcar.forward()
    time.sleep(1)
    pcar.turn(turn_duration)
    pcar.forward()
    time.sleep(60.0/forward_speed)
    pcar.backward_turn(backward_turn_duration)
    pcar.forward()
    time.sleep(280.0/forward_speed)
except:
    print('stopped')
    pcar.stop()
finally:
    print('stopped')
    pcar.stop()


