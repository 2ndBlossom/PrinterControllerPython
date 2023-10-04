import time

def estop(x, y, z, vx, vz):
    axis = '1'
    mov = 3
    vmax = 22.5
    tx = mov/vmax
    tz = mov/vmax
    movx = 20      # if out of range, move x to 20 mm
    movy = 3       # if out of range, move y by 3 mm
    movz = 1       # if out of range, move z by 1 mm
    movt = mov + movz
    tz2 = movt/vmax

    # x.HLT(axis);
    # y.HLT(axis);
    # z.HLT(axis);   zpy: HLT [{<AxisID>}] Halt Motion Smoothly (p. 172)

    x.STP()
    y.STP()
    z.STP()
    pos = z.qPOS(axis)

    if pos < (51-mov) and pos > mov:
        x.VEL(axis, vmax)
        z.VEL(axis, vmax)
        z.MVR(axis, -mov)
        time.sleep(tz)
        
        if x.qPOS(axis) < 100 and y.qPOS(axis) >= 26:
            x.MVR(axis, mov)
            time.sleep(tx)
            z.MVR(axis, mov)
            time.sleep(tz)
            
        elif x.qPOS(axis) >= 100 and y.qPOS(axis) >= 28:
            
            z.MVR(axis, -movz)
            y.MVR(axis, -movy)
            x.MOV(axis, movx)

            while(0 != x.IsMoving()):
                time.sleep(0.1)

            z.MVR(axis, movt)
            time.sleep(tz2); 
    else:
        print("Z Out of range")

    z.HLT(axis)
    x.HLT(axis)
    y.HLT(axis)

    x.VEL(axis, vx)
    z.VEL(axis, vz)

   