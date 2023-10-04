from delay import delay

def PMoveX(x, vx, distance):
    axis = '1'
    x_limit = 102
    x_limit2 = 0

    pos = x.qPOS(axis)
    pos += distance

    if vx != 0 or vx:
        Wx = abs(distance / vx)
        if x_limit2 <= pos < x_limit:
            x.MVR(axis, distance)
            delay(Wx)
        else:
            print("X Out of range")

def PMoveY(y, vy, distance):
    axis = '1'
    y_limit = 102
    y_limit2 = 0

    pos = y.qPOS(axis)
    pos += distance

    if vy != 0 or vy:
        Wy = abs(distance / vy)
        if y_limit2 <= pos < y_limit:
            y.MVR(axis, distance)
            delay(Wy)
        else:
            print("Y Out of range")

def PMoveZ(z, vz, distance):
    distance = -distance
    axis = '1'
    z_limit = 102
    z_limit2 = 0

    pos = z.qPOS(axis)
    pos += distance

    if vz != 0 or vz:
        Wz = abs(distance / vz)
        if z_limit2 <= pos < z_limit:
            z.MVR(axis, distance)
            delay(Wz)
        else:
            print("Z Out of range")
