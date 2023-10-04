def moveX(x, distance):
    axis = '1'
    x_limit = 102
    x_limit2 = 0

    pos = x.qPOS(axis)
    pos += distance

    if x_limit2 <= pos < x_limit:
        x.MVR(axis, distance)
    else:
        print("X Out of range")

def moveY(y, distance):
    axis = '1'
    y_limit = 101
    y_limit2 = 1

    pos = y.qPOS(axis)
    pos += distance

    if y_limit2 <= pos < y_limit:
        y.MVR(axis, distance)
    else:
        print("Y Out of range")

def moveZ(z, distance):
    axis = '1'
    z_limit = 52
    z_limit2 = 0

    pos = z.qPOS(axis)
    pos += distance

    if z_limit2 <= pos < z_limit:
        z.MVR(axis, distance)
    else:
        print("Z Out of range")