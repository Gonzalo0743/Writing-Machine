import pyfirmata



def move_servo(angle):
    board = pyfirmata.Arduino('COM5')
    pin9 = board.get_pin('d:9:s')
    pin9.write(angle)


def main():
    global pin9

    board = pyfirmata.Arduino('COM5')

    iter8 = pyfirmata.util.Iterator(board)
    iter8.start()

    pin9 = board.get_pin('d:9:s')
