import time
def third_space(x,y,z,vx,vy,vz):

    s = 1

    axis = '1'

    if x.qPOS(axis) < 85:
        if (vy != 0 and vx != 0) or (vy and vx):
            Ws = s/vx
        else:
            Wi = 0
            Wq = 0
        x.MVR(axis, s)
        time.sleep(Ws)
        
    elif x.qPOS(axis) >= 85 and y.qPOS(axis) >= 7:
        #set_param('wave2','SimulationCommand','stop');
        x.VEL(axis, 22.5)
        z.MVR(axis, -1)
        y.MVR(axis, -7)
        x.MOV(axis, 20)
        
        while x.IsMoving():
            time.sleep(0.1)

        x.VEL(axis, vx)
        z.MVR(axis, 1)
    #set_param('wave2','SimulationCommand','stop');