from pyfirmata import Arduino, util
import time

port = "COM3"

board = Arduino(port)

iterator = util.Iterator(board)
iterator.start()

direction_pin = board.get_pin('d:13:o')
speed_pin = board.get_pin('d:11:p')
brake_pin = board.get_pin('d:8:o')
time.sleep(1.0)

while True:
    brake_pin.write(0)
    direction_pin.write(0)
    print("Direction CCW")
    speed_pin.write(0.15)
    print("Speed 30")
    time.sleep(5)

    brake_pin.write(1)
    print("Break applied")
    time.sleep(5)

    brake_pin.write(0)
    print("Brake Released")
    direction_pin.write(1)
    print("Direction CW")
    speed_pin.write(1)
    print("Speed 30")
    time.sleep(5)
    brake_pin.write(1)
    time.sleep(5)
board.exit()