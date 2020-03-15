from pyfirmata import Arduino, util
import numpy as np
import math
import time


class stepper_motor:

    def __init__(self):

        self.port = "COM3"

        self.board = Arduino(self.port)
        time.sleep(3.0)
        iterator = util.Iterator(self.board)
        iterator.start()

        # Initialize Pins or Motor Shield
        self.pwmA = self.board.get_pin('d:3:p')
        self.pwmB = self.board.get_pin('d:11:p')
        self.brakeA = self.board.get_pin('d:9:o')
        self.brakeB = self.board.get_pin('d:8:o')
        self.dirA = self.board.get_pin('d:12:o')
        self.dirB = self.board.get_pin('d:13:o')

        # Release Brakes and set PMW
        self.pwmA.write(1)
        self.pwmB.write(1)
        self.brakeA.write(0)
        self.brakeB.write(0)

        # Dimension of Instruments
        self.radiusMotor = 0.03  # in meters
        self.radiusTube = 0.0015  # in meters
        self.steps = 200  # numbers of step of the stepper_motor per rotation

    def clockwiseStep(self, sleepTime):
        time.sleep(sleepTime)
        self.dirA.write(1)
        time.sleep(sleepTime)
        self.dirB.write(1)
        time.sleep(sleepTime)
        self.dirA.write(0)
        time.sleep(sleepTime)
        self.dirB.write(0)

    def counterClockwiseStep(self, sleep):
        time.sleep(sleep)
        self.dirB.write(0)
        time.sleep(sleep)
        self.dirA.write(0)
        time.sleep(sleep)
        self.dirB.write(1)
        time.sleep(sleep)
        self.dirA.write(1)

    def calcVolume(self, volume):

        stepsPerRotation = self.steps / 4  # necessary to divide for granularity
        circOfMotor = 2 * math.pi * self.radiusMotor
        height = volume / (math.pi * self.radiusTube ** 2)
        numberOfRotation = height / circOfMotor

        rotationParameter = stepsPerRotation * numberOfRotation

        return rotationParameter

    def aspiration(self, volume):
        rotationParameter = self.calcVolume(volume)
        for i in range(0, int(rotationParameter), 1):
            self.clockwiseStep(0.004)

    def dispensation(self, volume):
        rotationParameter = self.calcVolume(volume)
        for j in range(0, int(rotationParameter), 1):
            self.counterClockwiseStep(0.004)
