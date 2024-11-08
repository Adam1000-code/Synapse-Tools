import os
import globals
from time import sleep

globals.ClearScreen()

print("what would you like to call this game object and it's class?")
headerName = input(">")

print("creating header...")

sleep(2)

f = open(headerName + ".hpp", "w")
f.write("""#pragma once

#include "../object/gameobject.hpp"
#include <iostream>
#include <string>

class {} : public GameObject
{{
    public:
        {}(Properties* props) : GameObject(props)
        {{
        }}

        virtual void Draw() = 0;
        virtual void Update(float deltaTime) = 0;
        virtual void Clean() = 0;
    
    protected:
        string m_name;
}};
""".format(headerName, headerName))
f.close()

print("done! you can now drag this file into the source code for the engine")

sleep(1)

os.system("python3 tools.py")