import time
def second_patternLayer(x,y,z,vx,vy,vz):
    axis = '1'
    W1 = 1.9/22
    W2 = 1/vz

    if x.qPOS(axis) < 85: # zpy: what's connections between patternLayer.m and pattern.m?
        x.VEL(axis, 22)
        z.MVR(axis, -1)
        time.sleep(W2)
        x.MVR(axis, -1.9)
        time.sleep(W1)
        x.VEL(axis, vx)
        z.MVR(axis, 1)
        time.sleep(W2)