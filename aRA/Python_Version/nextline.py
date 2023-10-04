def nextline(x, y, z, vx, vy, vz):
    movx = 20  # if out of range, move x to 20 mm
    movy = 6   # if out of range, move y by 6 mm
    movz = 1   # if out of range, move z by 1 mm
    axis = '1'

    posz = z.qPOS(axis)
    print(posz)


    #no set_param() in Python, bcz it is used for Simulink
    #set_param('wave2','SimulationCommand','stop') # You can implement this if needed.

    x.VEL(axis, 22.5)
    y.VEL(axis, 22.5)
    z.VEL(axis, 22.5)

    if posz < 51:
        z.MVR(axis, -movz)

    y.MVR(axis, -movy)
    x.MOV(axis, movx)

    # while x.IsMoving() - Uncomment and implement this if needed.
    #     pass

    z.MVR(axis, movz)

    x.VEL(axis, vx)
    y.VEL(axis, vy)
    z.VEL(axis, vz)