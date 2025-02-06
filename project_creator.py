import os
import globals
import json
import subprocess
from time import sleep

globals.ClearScreen()

print("Use a stable version or nightly build of the engine for the project?")
print("Nightly version is directly cloned by git from the Synapse Engine repository and has a good chance of containing bugs.")
print("""1. Stable
2. Nightly
Please enter the number 1 or 2 for your selected version""")

engineType = input("> ")

if engineType == "1":
    print("ERROR: unable to get latest release of the engine")
elif engineType == 2:
    subprocess.call(["git", "clone", "https://github.com/Adam1000-code/Synapse-Engine.git"])

print("What would you like your project to be called?")

projName = input("> ")

if projName == "":
    projName = "Default Project"

print("What is the name of the creator?")

creator = input("> ")

if creator == "":
    creator = "Synapse"

print("What should the project ID be? Ex: Synapse-Project")

id = input("> ")

print("What version of your game are you starting out with? (Leave blank for 0.1)")

ver = input("> ")

if ver == "":
    ver = 0.1

dir = projName
srcDir = os.path.join(dir, "src")

if not os.path.exists(dir):
    os.mkdir(dir)
if not os.path.exists(srcDir):
    os.mkdir(srcDir)

idFile = os.path.join(dir, "project.json")

projectSettings = {
    "Project": [
        {
            "Name": projName,
            "Creator": creator,
            "Version": ver,
            "ID": id
        }
    ]
}

with open(idFile, "w") as f:
    json.dump(projectSettings, f, indent=4)

print("Do you want the main file to be automatically created?")

answer = input("y or n: ")

if answer == "y" or answer == "Y":
    mainFile = os.path.join(srcDir, "main.cpp")
    with open(mainFile, "w") as f:
        f.write("""#pragma region Synapse Essentials

#include "core/engine.hpp"

#pragma endregion Synapse Essentials

/*----------------------------------------------------------------------------*/
/*                                                                            */
/*    Module:       main.cpp                                                  */
/*    Author:       {{Author}}                                                */
/*    Description:  Synapse Engine Project                                    */
/*                                                                            */
/*----------------------------------------------------------------------------*/

#include <iostream>

int main()
{
    return 0;
}
""")

print("done! your project has been created!")

sleep(2)

os.system("python3 tools.py")