import os
import globals
import json
from time import sleep

globals.ClearScreen()

print("What would you like your project to be called?")

projName = input(">")

if projName == "":
    projName = "Default Project"

print("What is the name of the creator?")

creator = input(">")

if creator == "":
    creator = "Synapse"

print("What should the project ID be? Ex: Synapse-Project")

id = input(">")

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
            "ID": id
        }
    ]
}

with open(idFile, "w") as f:
    json.dump(projectSettings, f, indent=4)

print("Do you want the main file to be automatically created?")

answer = input("y or n:")

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