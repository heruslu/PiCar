from picar import front_wheels
from picar import back_wheels

class Wheels:
    def __init__(self):
        self.front = front_wheels.Front_Wheels(db='config')
        self.back = back_wheels.Back_Wheels(db='config')        


class Car:
    def __init__(self,wheels,speed=None,direction=None,angle=None,sensor=None):
        self.wheels = wheels
        self.speed= speed
        self.direction = direction
        self.angle = angle
        self.sensor = sensor