import time
def third_pattern(x,y,z,vx,vy,vz):
    i = 2.5
    j = 0.4
    k = 2*j

    a = i-j
    b = i-0.8
    c = i-1.2
    d = i-1.6
    e = i-2
    v1 = vx            ### multplication factor here

    axis = '1'

    # set_param('wave2','SimulationCommand','start');
    time.sleep(0.2)

    if x.qPOS(axis) < 85:
        if (vy != 0 and vx != 0) or (vy and vx):
            Wi = i/vy          # wait time for Y movement
            Wa = a/vy
            Wb = b/vy
            Wc = c/vy
            Wd = d/vy
            We = e/vy
            Wk = k/vy
            Wz = 1/vz
            
            Wi2 = i/v1
            Wa2 = a/v1
        else:
            Wi = 0
            Wq = 0
        
        x.VEL(axis, v1)
        y.VEL(axis, v1)
        
        y.MVR(axis, i)
        time.sleep(Wi2)
        
        x.MVR(axis, i)
        time.sleep(Wi2)
        
        y.MVR(axis, -i)
        time.sleep(Wi2)                  # first block
        
        x.VEL(axis, vx)
        y.VEL(axis, vy)
        
        x.MVR(axis, -a)
        time.sleep(Wa)
        
        y.MVR(axis, a)
        time.sleep(Wa)
        
        x.MVR(axis, b)
        time.sleep(Wb)
        
        y.MVR(axis, -b)
        time.sleep(Wb)                  # second block
        
        x.MVR(axis, -c)
        time.sleep(Wc)
            
        y.MVR(axis, c)
        time.sleep(Wc)
        
        x.MVR(axis, d)
        time.sleep(Wd)
        
        y.MVR(axis, -d)
        time.sleep(Wd)                  # third block finish
        
        x.MVR(axis, -e)
        time.sleep(We)
        
        set_param('wave2','SimulationCommand','stop')
        time.sleep(0.1)

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