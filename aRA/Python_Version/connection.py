import os
import time
from pipython import GCS2Device
#from pipython import GCS2Controller

def connection():
    controllerSerialNumberM = '0023550267'  # X - axis, top stage
    #controllerSerialNumberF = '0021550261'  # Y - axis, limit 20mm, bottom stage
    #controllerSerialNumberZ = '0021550262'  # Z - axis, 0 is up 52 (down)

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

    print('Cleared: Load GCS Libraries')

    # Connect to PI devices
    PIdevice = GCS2Device(controllerSerialNumberM)
    PIdevice.InterfaceSetupDlg()
    
    #PIdevice2 = GCS2Device(controllerSerialNumberF)
    #PIdevice3 = GCS2Device(controllerSerialNumberZ)

    print(PIdevice.qIDN())
    #print(PIdevice2.qIDN())
    #print(PIdevice3.qIDN())

    # Initialize PI devices
    #PIdevice.InitializeController()
    #PIdevice2.InitializeController()
    #PIdevice3.InitializeController()

    # Startup stage - switch servo on for axis
    switchOn = 1
    PIdevice.SVO(axis, switchOn)
    #PIdevice2.SVO(axis, switchOn)
    #PIdevice3.SVO(axis, switchOn)

    # Return connected devices and controller
    return PIdevice#, PIdevice2, PIdevice3