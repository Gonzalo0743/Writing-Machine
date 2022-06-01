import pyfirmata
import time

speedRight = 85
speedLeft = 105
noSpeed = 90

posAxisX = 0
posAxisY = 0

# Pos(X,Y):::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def pos(x, y):
    global posAxisX, posAxisY
    posX(x)
    posY(y)
    return

# Pos::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def posX(coor):
    global posAxisX
    move = coor - posAxisX
    if move < 0:
        continueLeft(move)
        return
    if move > 0:
        continueRight(move)
        return
    else:
        return

def posY(coor):
    global posAxisY
    move = coor - posAxisY
    if move < 0:
        continueDown(move)
        return
    if move > 0:
        continueUp(move)
        return
    else:
        return


# ContiueRight/Left/Up/Down:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def continueRight(units):
    global posAxisX
    pin9.write(speedRight)
    time.sleep(units)
    pin9.write(noSpeed)
    posAxisX += units
    print(posAxisX)
    return

def continueLeft(units):
    global posAxisX
    pin9.write(speedLeft)
    time.sleep(units)
    pin9.write(noSpeed)
    posAxisX -= units
    print(posAxisX)
    return

#Cambiar Pin
def continueUp(units):
    global posAxisY
    pin9.write(speedLeft)
    time.sleep(units)
    pin9.write(noSpeed)
    posAxisY += units
    print(posAxisY)
    return

#Cambiar Pin
def continueDown(units):
    global posAxisY
    pin9.write(speedLeft)
    time.sleep(units)
    pin9.write(noSpeed)
    posAxisY -= units
    print(posAxisY)
    return
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

def main():
    global pin9
    units = 5

    board = pyfirmata.Arduino('COM5')

    iter8 = pyfirmata.util.Iterator(board)
    iter8.start()

    pin9 = board.get_pin('d:9:s')
    continueRight(units)

main()
