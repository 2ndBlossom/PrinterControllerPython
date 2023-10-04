import os
import time
from pipython import GCS2Device, pitools
#from pipython import GCS2Controller

def connection():
    controllerSerialNumberM = '0023550267'  # X - axis, top stage
    controllerSerialNumberF = '0021550261'  # Y - axis, limit 20mm, bottom stage
    controllerSerialNumberZ = '0021550262'  # Z - axis, 0 is up 52 (down)


    STAGES = None
    REFMODE = None
    axis = '1'

    # Load PI MATLAB Driver GCS2
    #any (os.name == 'nt')

    #if not isWindows:
    #    os.environ['LD_LIBRARY_PATH'] = '/usr/qin/PI/pi_matlab_driver_gcs2'

    # Load PI_GCS_Controller if not already loaded
    #if 'Controller' not in locals():
    #    Controller = GCS2Controller()
    #if not isinstance(Controller, GCS2Controller):
    #    Controller = GCS2Controller()

    # Connect to PI devices
    PIdevice = GCS2Device()
    PIdevice.ConnectUSB(controllerSerialNumberM)
    pitools.startup(PIdevice, stages=STAGES, refmodes=REFMODE)
    print(PIdevice.qIDN())

    PIdevice2 = GCS2Device()
    PIdevice2.ConnectUSB(controllerSerialNumberF)
    pitools.startup(PIdevice2, stages=STAGES, refmodes=REFMODE)
    print(PIdevice2.qIDN())

    PIdevice3 = GCS2Device()
    PIdevice3.ConnectUSB(controllerSerialNumberZ)
    pitools.startup(PIdevice3, stages=STAGES, refmodes=REFMODE)
    print(PIdevice3.qIDN())

    # Startup stage - switch servo on for axis
    switchOn = 1
    PIdevice.SVO(axis, switchOn)
    #PIdevice2.SVO(axis, switchOn)
    #PIdevice3.SVO(axis, switchOn)

    # Return connected devices and controller
    return PIdevice, PIdevice2, PIdevice3