from delay import delay

def position(x, y, z):
    axis = '1'

    # Check if any axis is moving (you can uncomment these lines if needed)
    # while x.IsMoving() or y.IsMoving() or z.IsMoving():
    #     pass

    posx = x.qPOS(axis)
    posy = y.qPOS(axis)
    posz = z.qPOS(axis)

    posz = 52 - posz  # Adjust the 'posz' value as in the MATLAB code

    # Convert position values to strings (you can remove this if not needed)
    posx = str(posx)
    posy = str(posy)
    posz = str(posz)

    return posx, posy, posz

def PosUpdate():
    while True:
        posx, posy, posz = position(x, y, z)
        print(f"Position X: {posx}, Position Y: {posy}, Position Z: {posz}")
        delay(0.1)