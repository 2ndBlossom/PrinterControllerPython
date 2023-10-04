def ToExit(x,y,z):
    axis = '1'
    switchOff = 0

    x.SVO ( axis, switchOff ) #zpy: SVO {<AxisID> <MotorState>} Set Motor State
    y.SVO ( axis, switchOff )
    z.SVO ( axis, switchOff )

    x.CloseConnection ()
    x.Destroy ()
    del x
    #y.CloseConnection (); y.Destroy (); del y;
    #z.CloseConnection (); z.Destroy (); del z;
    #controller.Destroy(); del controller