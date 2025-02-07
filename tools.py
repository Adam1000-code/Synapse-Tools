import os
import sys
import globals

def MainModule():
    print("type ver for version and quit to exit the program")
    print("1. New GameObject header file")
    print("2. New Synapse Engine Project")
    
    option = input(">")

    match option:
        case "ver":
            os.system("python3 version.py")
        case "quit":
            sys.exit(0)
        case "1":
            os.system("python3 gameobject_header.py")
        case "2":
            os.system("python3 project_creator.py")

globals.ClearScreen()

print("Synapse Tools: For the Synapse Engine")

while True:
    MainModule()