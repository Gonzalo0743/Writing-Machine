import pyfirmata
import time

# Servo speed
speedPosX = 85   # Positive X
speedNegX = 93   # Negative X

speedPosY = 85   # Positive Y
speedNegY = 95   # Negative Y

noSpeed = 90     # Stop

# Initial axis positions
with open('memoryAxis.txt', 'r') as memoryAxis:
    axisPositions = memoryAxis.readlines()
posAxisX = int(axisPositions[0])
posAxisY = int(axisPositions[1])


# Pen servo positions and state
## Cambiar pen
penUp = 5
penDown = 0
isPenUp = True

# Axis limits
limitLeftX = 0
limitRightX = 15
limitDownY = 0
limitUpY = 20

## Estorba probablemente
global pinX, pinY


board = pyfirmata.Arduino('COM3')
iter8 = pyfirmata.util.Iterator(board)
iter8.start()

# Pins setup
## Cambiar Pen
pinX = board.get_pin('d:10:s')
pinY = board.get_pin('d:9:s')
pinPen = board.get_pin('d:8:s')
pinPen.write(penUp)
pinX.write(90)
pinY.write(90)

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
        continueLeft(abs(move))
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
        continueDown(abs(move))
        return
    if move > 0:
        continueUp(move)
        return
    else:
        return


# ContiueRight/Left/Up/Down:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def continueRight(units):
    global posAxisX
    expectedMove = posAxisX + units
    if expectedMove >= limitRightX:
        excess = expectedMove - limitRightX
        move = units - excess
    else:
        move = units
    if move == 0:
        print('Comando ejecutado, posicion actual en x: ', posAxisX)
        return
    else:
        moveTime = move / 10
        pinX.write(speedPosX)
        time.sleep(moveTime)
        pinX.write(noSpeed)
        posAxisX += move
        axisPositions[0] = str(posAxisX) + '\n'
        with open('memoryAxis.txt', 'w') as memoryAxis:
            memoryAxis.writelines(axisPositions)

        return

def continueLeft(units):
    global posAxisX
    expectedMove = posAxisX - units
    if expectedMove <= limitLeftX:
        excess = expectedMove + abs(limitLeftX)
        move = units - abs(excess)
    else:
        move = units
    if move == 0:
        print('Comando ejecutado, posicion actual en x: ', posAxisX)
        return
    else:
        moveTime = move / 10
        pinX.write(speedNegX)
        time.sleep(moveTime)
        pinX.write(noSpeed)
        posAxisX -= move
        axisPositions[0] = str(posAxisX) + '\n'
        with open('memoryAxis.txt', 'w') as memoryAxis:
            memoryAxis.writelines(axisPositions)
        print('Comando ejecutado, posicion actual en x: ', posAxisX)
        return


def continueUp(units):
    global posAxisY
    expectedMove = posAxisY + units
    if expectedMove >= limitUpY:
        excess = expectedMove - limitUpY
        move = units - excess
    else:
        move = units
    if move == 0:
        print('Comando ejecutado, posicion actual en y: ', posAxisY)
        return
    else:
        moveTime = move / 10
        pinY.write(speedPosY)
        time.sleep(moveTime)
        pinY.write(noSpeed)
        posAxisY += move
        axisPositions[1] = str(posAxisY) + '\n'
        with open('memoryAxis.txt', 'w') as memoryAxis:
            memoryAxis.writelines(axisPositions)
        print('Comando ejecutado, posicion actual en y: ', posAxisY)
        return

def continueDown(units):
    global posAxisY
    expectedMove = posAxisY - units
    if expectedMove <= limitDownY:
        excess = expectedMove + abs(limitDownY)
        move = units - abs(excess)
    else:
        move = units
    if move == 0:
        print('Comando ejecutado, posicion actual en y: ', posAxisY)
        return
    else:
        moveTime = move / 10
        pinY.write(speedNegY)
        time.sleep(moveTime)
        pinY.write(noSpeed)
        posAxisY -= move
        axisPositions[1] = str(posAxisY) + '\n'
        with open('memoryAxis.txt', 'w') as memoryAxis:
            memoryAxis.writelines(axisPositions)
        print('Comando ejecutado, posicion actual en y: ', posAxisY)
        return

# Up/Down:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

def up():
    global isPenUp
    if isPenUp != True:
        pinPen.write(penUp)
        isPenUp = True
        return
    else:
        return

def down():
    global isPenUp
    if isPenUp != False:
        pinPen.write(penDown)
        isPenUp = False
        return
    else:
        return




