import time

def next(x, y, z, vx, vy, vz):
    p = 1        # x axis move side
    q = 1        # z axis move up, negative sign for up movement
    movx = 15    # if out of range, move x to 20 mm
    movy = 5     # if out of range, move y by 4 mm
    movz = 1     # if out of range, move z by 1 mm
    axis = '1'
    vel = 10

    if (z.qPOS(axis) < 51) and (x.qPOS(axis) < 100) and (z.qPOS(axis) > 1):
        x.VEL(axis, vel)
        y.VEL(axis, vel)
        z.VEL(axis, vel)

        if (vx != 0 and vz != 0) or (vx and vz):
            Wx = p / vel         # wait time for 0.3 mm
            Wz = q / vel         # wait time for 1 mm up movement z axis
        else:
            Wy = 0
            Wy2 = 0
            q = 0
            i = 0
            Wx = 0
            p = 0

        z.MVR(axis, -q)
        time.sleep(Wz)

        x.MVR(axis, p)
        time.sleep(Wx)

        z.MVR(axis, q)

    elif (z.qPOS(axis) <= 51) and (x.qPOS(axis) >= 100) and (y.qPOS(axis) >= 7):
        # set_param('wave2','SimulationCommand','stop') - You can implement this if needed.
        x.VEL(axis, 22.5)
        z.MVR(axis, -movz)
        y.MVR(axis, -movy)
        x.MOV(axis, movx)

        while x.IsMoving():
            time.sleep(0.1)

        x.VEL(axis, vx)
        z.MVR(axis, movz)
        return

    else:
        print('Next distance out of range')

    x.VEL(axis, vx)
    y.VEL(axis, vy)
    z.VEL(axis, vz)