import os
import globals
from time import sleep

globals.ClearScreen()

print("Synapse Tools version {}.{}, created by {}".format(globals.toolsMajorVer, globals.toolsMinorVer, globals.creator))

sleep(2)

os.system("python3 tools.py")