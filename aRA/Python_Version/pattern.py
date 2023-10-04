import time

def pattern(x, y, z, vx, vy, vz):
    p = 0.2
    q = 0.8         # length
    r = 0
    i = 1.5
    s = 1
    movx = 20       # if out of range, move x to 20 mm
    movy = 4        # if out of range, move y by 4 mm
    movz = 1        # if out of range, move z by 1 mm
    axis = '1'

    # set_param('wave2','SimulationCommand','start') - You can implement this if needed.
    time.sleep(0.1)

    if x.qPOS(axis) < 100 and y.qPOS(axis) >= 26:
        if (vy != 0 and vx != 0) or (vy and vx):
            Wy = i / vy     # wait time for 2 mm
            Wy2 = q / vy    # wait time for 1 mm
            Wx = p / vx     # wait time for 0.3 mm

        else:
            Wy = 0
            Wy2 = 0
            q = 0
            i = 0
            Wx = 0
            p = 0

        y.MVR(axis, i)
        time.sleep(Wy)

        while r < s:
            x.MVR(axis, p)
            time.sleep(Wx)
            r = r + p

            if r >= s:
                y.MVR(axis, -i)
                time.sleep(Wy)
                break

            y.MVR(axis, -q)
            time.sleep(Wy2)

            x.MVR(axis, p)
            time.sleep(Wx)
            r = r + p

            y.MVR(axis, q)
            time.sleep(Wy2)

    elif x.qPOS(axis) >= 100 and y.qPOS(axis) >= 28:
        # set_param('wave2','SimulationCommand','stop') - You can implement this if needed.
        x.VEL(axis, 22.5)
        z.MVR(axis, -movz)
        y.MVR(axis, -movy)
        x.MOV(axis, movx)

        while x.IsMoving():
            time.sleep(0.1)

        x.VEL(axis, vx)
        z.MVR(axis, movz)
        
    # set_param('wave2','SimulationCommand','stop') - You can implement this if needed.