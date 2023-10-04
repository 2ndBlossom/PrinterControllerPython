def movXpos(x, position):
    axis = '1'
    if 0 <= position <= 102:
        x.MOV (axis, position)
    else:
        print("X Out of range")

def movYpos(y, position):
    axis = '1'
    if 22 <= position <= 102:
        y.MOV (axis, position)
    else:
        print("Y Out of range")

def movZpos(z, position):
    axis = '1'
    if 0 <= position <= 52:
        position = 52 - position
        z.MOV (axis, position)
    else:
        print("Z Out of range")