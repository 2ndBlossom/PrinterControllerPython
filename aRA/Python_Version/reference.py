def reference(x, y, z, vx, vy, vz):
    axis = '1'
    vel = 22

    print('Referencing the stages')

    x.VEL(axis, vel)
    y.VEL(axis, vel)
    z.VEL(axis, vel)

    x.FRF(axis) #zpy: FRF FRF [{<AxisID>}] Starts a reference move to the reference switch.
                # The approach depends on the value of the
                #Reference Signal Type parameter (ID 0x70):
                #0 or 1: The approach is always done from the
                #same side irrespective of the axis position
                #when the command is sent.
                #2: The approach is done via the negative limit
                #switch.
    y.FRF(axis)
    #z.FRF(axis);
    z.FNL(axis)

    while y.IsMoving() or z.IsMoving():
        pass

    print('Referenced')

    x.VEL(axis, vx)
    y.VEL(axis, vy)
    z.VEL(axis, vz)