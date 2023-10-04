def stop(x, y, z):
    axis = '1'

    # x.HLT(axis);
    # y.HLT(axis);
    # z.HLT(axis);

    x.STP()
    y.STP()
    z.STP()