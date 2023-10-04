import time
def third_patternLayer(x,y,z,vx,vy,vz):

    i = 2.5
    j = 0.4
    k = 2*j

    c = i-1.2

    f = 1.2

    axis = '1'

    if x.qPOS(axis) < 85:
        if (vy != 0 and vx != 0) or (vy and vx):
            Wc = c/vy
            Wk = k/vy
            Wz = 1/vz
        else:
            Wi = 0
            Wq = 0
        
        x.VEL(axis, 22)
        y.VEL(axis, 22)
        
        z.MVR(axis, -1)
        time.sleep(Wz)
        
        y.MVR(axis, -k)
        time.sleep(Wk)
        
        x.MVR(axis, -f)
        time.sleep(Wc)
        
        z.MVR(axis, 1)
        time.sleep(Wz)
        
        x.VEL(axis, vx)
        y.VEL(axis, vy)