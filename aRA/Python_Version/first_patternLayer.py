import time

def first_patternLayer(x,y,z,vx,vy,vz):

    axis = '1'
    W1 = 3.5/22
    W2 = 1/vz

    if x.qPOS(axis) < 85:
        x.VEL(axis, 22)
        z.MVR(axis, -1) #zpy: if we don't set Velocity, what's the speed of command MVR?
        time.sleep(W2)
        x.MVR(axis, -3.5)
        time.sleep(W1)
        x.VEL(axis, vx)
        z.MVR(axis, 1)
        time.sleep(W2)
