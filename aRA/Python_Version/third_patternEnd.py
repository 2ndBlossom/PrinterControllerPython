import time
def third_patternEnd(x,y,z,vx,vy,vz): #zpy: what does this END.m do? set the stage to initial positin?
    i = 2.5
    j = 0.4
    k = 2*j

    a = i-j
    b = i-0.8
    c = i-1.2
    d = i-1.6
    e = i-2

    axis = '1'

    #set_param('wave2','SimulationCommand','stop');

    if x.qPOS(axis) < 85:
        if (vy != 0 and vx != 0) or (vy and vx):#zpy: why we need to set different time.sleep time?
            Wc = c/vy
            Wk = k/vy
            Wz = 1/vz
        else:
            Wi = 0
            Wq = 0

        z.MVR(axis, -1)
        time.sleep(Wz)
        
        y.MVR(axis, -k)
        time.sleep(Wk)
        
        x.MVR(axis, c)
        time.sleep(Wc)
        
        z.MVR(axis, 1)
        time.sleep(Wz)