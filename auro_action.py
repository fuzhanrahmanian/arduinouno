# import sys

# sys.path.append(r'../drivers')

# from drivers.arduino import ArduinoUno
from auro_driver import ArduinoUno
import time

confd = {'direction_pin': 'd:13:o', 'speed_pin': 'd:11:p', 'brake_pin': 'd:8:o'}


class pump:
    def __init__(self):
        self.driver_arduino = ArduinoUno()
        self.direction_pin = self.driver_arduino.board().get_pin(confd['direction_pin'])
        self.speed_pin = self.driver_arduino.board().get_pin(confd['speed_pin'])
        self.brake_pin = self.driver_arduino.board().get_pin(confd['brake_pin'])

    def DC_motor_cw(self, speed, pause=5, direction=1):  # speed can be a value between 0 and 1
        self.driver_arduino.iterative_move()
        self.brake_pin.write(0)
        print("Brake Released")
        self.direction_pin.write(direction)
        print("Direction CW")
        self.speed_pin.write(speed)
        print("Speed 30")
        time.sleep(pause)
        self.brake_pin.write(1)
        time.sleep(pause)
        self.driver_arduino.board().exit()

    def DC_motor_ccw(self, speed, pause=5, direction=0):
        self.driver_arduino.iterative_move()
        self.brake_pin.write(0)
        print('Brake Released')
        self.direction_pin.write(direction)
        print("Direction CCW")
        self.speed_pin.write(speed)
        print("Speed 30")
        time.sleep(pause)
        self.brake_pin.write(1)
        print("Break applied")
        time.sleep(pause)
        self.driver_arduino.board().exit()

    def measure_force(self):
        pass
