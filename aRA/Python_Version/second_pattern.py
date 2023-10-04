import time
def second_pattern(x,y,z,vx,vy,vz):
    i = 3
    j = 1

    p = 0.3
    q = 0.4
    r = 0.5
    v1 = vx                ### multplication factor here

    axis = '1'

    # set_param('wave2','SimulationCommand','start');
    time.sleep(0.2)

    if x.qPOS(axis) < 85:
        if (vy != 0 and vx != 0) or (vy and vx):
            Wi = i/vy          # wait time for Y movement
            Wj = j/vy        
            
            Wp = p/vx          # wait time for X movement
            Wq = q/vx
            Wr = r/vx
            
            Wi2 = i/v1
            Wp2 = p/v1
        else:
            Wi = 0
            Wq = 0
        
        x.VEL(axis, v1)
        y.VEL(axis, v1)
        
        y.MVR(axis, i)
        time.sleep(Wi2)
        
        x.MVR(axis, p)
        time.sleep(Wp2)
        
        x.VEL(axis, vx)
        y.VEL(axis, vy)
        
        y.MVR(axis, -j)
        time.sleep(Wj)                  # first block
        
        x.MVR(axis, q)
        time.sleep(Wq)
        
        y.MVR(axis, j)
        time.sleep(Wj)
        
        x.MVR(axis, r)
        time.sleep(Wr)
        
        y.MVR(axis, -j)
        time.sleep(Wj)                  # second block
        
        x.MVR(axis, q)
        time.sleep(Wq)
            
        y.MVR(axis, j)
        time.sleep(Wj)
        
        x.MVR(axis, p)
        time.sleep(Wp)
        
        y.MVR(axis, -i)
        time.sleep(Wi)                  # third block finish
        
        # set_param('wave2','SimulationCommand','stop');
        
    elif x.qPOS(axis) >= 85 and y.qPOS(axis) >= 7:
        #set_param('wave2','SimulationCommand','stop');
        
        x.VEL(axis, 22.5)
        z.MVR(axis, -1)
        y.MVR(axis, -6)
        x.MOV(axis, 20)
        
        while(x.IsMoving()):
            time.sleep(0.1)
        
        x.VEL(axis, vx)
        z.MVR(axis, 1)

    #set_param('wave2','SimulationCommand','stop');