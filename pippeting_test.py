from stepper_motor import stepper_motor

# Import Stepper Motor
sm = stepper_motor()

# Aspiration in liters
sm.aspiration(0.0000020)

# Dispensation in liters
sm.dispensation(0.0000020)

# Close Arduino Board
sm.board.exit()
