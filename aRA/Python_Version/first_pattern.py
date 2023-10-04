import time

def first_pattern(x, y, z, vx, vy, vz):
    i = 1.5
    j = 2.5
    k = 4

    q = 0.5
    r = 1
    v1 = vx     # multplication factor here
    axis = '1'

    # set_param('wave2','SimulationCommand','start') - You can implement this if needed.
    time.sleep(0.2)

    if x.qPOS(axis) < 85:
        if (vy != 0 and vx != 0) or (vy and vx):
            Wi = i / vy     # wait time for Y movement
            Wj = j / vy
            Wk = k / vy

            Wq = q / vx     # wait time for X movement
            Wr = r / vx

            Wi2 = i / v1
            Wq2 = q / v1
        else:
            Wi = 0
            Wq = 0

        x.VEL(axis, v1)
        y.VEL(axis, v1)

        y.MVR(axis, i)
        time.sleep(Wi2)

        x.MVR(axis, q)
        time.sleep(Wq2)

        y.MVR(axis, -i)
        time.sleep(Wi2)     # first block

        x.VEL(axis, vx)
        y.VEL(axis, vy)

        x.MVR(axis, r)
        time.sleep(Wr)

        y.MVR(axis, j)
        time.sleep(Wj)      # second block

        x.MVR(axis, q)
        time.sleep(Wq)

        y.MVR(axis, -j)
        time.sleep(Wj)

        x.MVR(axis, r)
        time.sleep(Wr)

        y.MVR(axis, k)
        time.sleep(Wk)

        x.MVR(axis, q)
        time.sleep(Wq)

        y.MVR(axis, -k)
        time.sleep(Wk)      # third block finish

        # set_param('wave2','SimulationCommand','stop') - You can implement this if needed.

    elif x.qPOS(axis) >= 85 and y.qPOS(axis) >= 7:
        # set_param('wave2','SimulationCommand','stop') - You can implement this if needed.
        x.VEL(axis, 22.5)
        z.MVR(axis, -1)
        y.MVR(axis, -6)
        x.MOV(axis, 20)

        while x.IsMoving():
            time.sleep(0.1)

        x.VEL(axis, vx)
        z.MVR(axis, 1)

    # set_param('wave2','SimulationCommand','stop') - You can implement this if needed.