#pragma once

#include "character.hpp"
#include "../animation/spriteanimation.hpp"
#include "../physics/rigidbody.hpp"
#include "../physics/collider.hpp"

#define JUMP_TIME 15.0f
#define JUMP_FORCE 10.0f
#define RUN_FORCE 4.0f

# class Player : public Character
# {
#     public:
#         Player(Properties* props);

#         virtual void Draw();
#         virtual void Update(float deltaTime);
#         virtual void Clean();
    
#     private:
#         //int m_row, m_frame, m_frameCount;
#         //int m_animSpeed;
#         bool isJumping;
#         bool isGrounded;

#         float jumpForce;
#         float jumpTime;

#         Collider* m_collider;
#         RigidBody* m_rigidbody;
#         SpriteAnimation* m_animation;
#         Vector2D lastSafePos;
# };

import os
import globals
from time import sleep

f = open("characher.hpp", "w")
f.write("""#pragma once

#include "../object/gameobject.hpp"
#include <iostream>
#include <string>

class Character : public GameObject
{
    public:
        Character(Properties* props) : GameObject(props)
        {
        }

        virtual void Draw() = 0;
        virtual void Update(float deltaTime) = 0;
        virtual void Clean() = 0;
    
    protected:
        string m_name;
};
""")
f.close()

f = open("player.hpp", "w")
f.write("""#pragma once

#include "character.hpp"
#include "../animation/spriteanimation.hpp"
#include "../physics/rigidbody.hpp"
#include "../physics/collider.hpp"

#define JUMP_TIME 15.0f
#define JUMP_FORCE 10.0f
#define RUN_FORCE 4.0f

class Player : public Character
{
    public:
        Player(Properties* props);

        virtual void Draw();
        virtual void Update(float deltaTime);
        virtual void Clean();
    
    private:
        //int m_row, m_frame, m_frameCount;
        //int m_animSpeed;
        bool isJumping;
        bool isGrounded;

        float jumpForce;
        float jumpTime;

        Collider* m_collider;
        RigidBody* m_rigidbody;
        SpriteAnimation* m_animation;
        Vector2D lastSafePos;
};
""")

f.close()