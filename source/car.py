from picar import front_wheels
from picar import back_wheels
import random, time

class Speed:
    def __init__(self, forward = 100, backward = 70):
        self.forward = forward
        self.backward = backward

class Wheels:
    def __init__(self, turning_max = 45):
        self.front = front_wheels.Front_Wheels(db='config')
        self.back = back_wheels.Back_Wheels(db='config')   
        self.front.turning_max = turning_max

class Direction:
    def __init__(
            self, 
            pcar,
            last_dir = 0, 
            last_angle = 90, 
            force_turning = 0
            ):
        '''
        force_turning : int
            0 = random direction, 1 = force left, 2 = force right, 3 = orderdly
        '''
        self.pcar = pcar
        self.last_dir = last_dir
        self.last_angle = last_angle
        self.force_turning = force_turning
    
    def random_dir(self):
        if self.force_turning == 0:
            _dir = random.randint(0, 1)
        elif self.force_turning == 3:
            _dir = not self.last_dir
            self.last_dir = _dir
            print('last dir  %s' % self.last_dir)
        else:
            _dir = self.force_turning - 1
        angle = (90 - self.pcar.wheels.front.turning_max) + \
        (_dir * 2 * self.pcar.wheels.front.turning_max)
        self.last_angle = angle
        return angle
    
    def opposite_angle(self):
        if self.last_angle < 90:
            angle = self.last_angle + 2* self.pcar.wheels.front.turning_max
        else:
            angle = self.last_angle - 2* self.pcar.wheels.front.turning_max
        self.last_angle = angle
        return angle

class Car:
    def __init__(
            self,
            wheels,
            speed = None,
            direction = None,
            sensor = None
            ):
        self.wheels = wheels
        self.speed= speed
        self.dir = direction
        self.sensor = sensor
    
    def backward(self):
        print( "backward")
        self.wheels.front.turn(self.dir.opposite_angle())
        self.wheels.back.backward()
        self.wheels.back.speed = self.speed.backward
        time.sleep(1)
        self.wheels.front.turn(self.dir.opposite_angle())
        self.wheels.back.forward()
        time.sleep(1)

    def backward_turn(self, duration):
        print( "backward turn")
        self.wheels.front.turn(self.dir.opposite_angle())
        self.wheels.back.backward()
        self.wheels.back.speed = self.speed.backward
        time.sleep(duration)
    
    def forward(self):
        self.wheels.front.turn_straight()
        self.wheels.back.forward()
        self.wheels.back.speed = self.speed.forward
    
    def random_turn(self):
        print("turn")
        self.wheels.front.turn(self.dir.random_dir())
        self.wheels.back.forward()
        self.wheels.back.speed = self.speed.forward
        time.sleep(1)
    
    def turn(self, duration):
        print("turn")
        self.wheels.front.turn(self.dir.random_dir())
        self.wheels.back.forward()
        self.wheels.back.speed = self.speed.forward
        time.sleep(duration)
    
    def neg_dist_handler(self,count,timeout):
        print('negative distance counter: %d'%count)
        self.wheels.front.turn_straight()
        if count > timeout:  # timeout, stop;
            self.wheels.back.stop()
        else:
            self.wheels.back.backward()
            self.wheels.back.speed = self.speed.forward
            count += 1
        return count
    
    def stop(self):
        self.wheels.back.stop()
        self.wheels.front.turn_straight()
    
    def avoidance(
            self,
            back_distance = 30, 
            turn_distance = 40, 
            timeout = 10
            ):
        print('start_avoidance')
        count = 0
        while True:
            distance = self.sensor.get_distance()
            print("distance: %scm" % distance)
            if distance > 0:
                count = 0
                if distance < back_distance: # backward
                    self.backward()
                elif distance < turn_distance: # turn
                    self.random_turn()
                else:
                    self.forward()
            else:						# forward
                count = self.neg_dist_handler(count,timeout)