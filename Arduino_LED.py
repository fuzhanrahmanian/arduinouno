import serial
import time
import pyfirmata
#from adafruit_motorkit import MotorKit
#import motor
#kit = MotorKit()

pin = 13
port = 'COM3'
board = pyfirmata.Arduino(port)
while True:
    board.digital[pin].write(1)
    print("SOS")
    time.sleep(0.9)  # delays for 9 seconds
    board.digital[pin].write(0)
    time.sleep(0.9)  # delays for 9 seconds

board.exit()