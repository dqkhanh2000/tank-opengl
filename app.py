WIDTH = 500
HEIGHT = 500
BACKGROUND_COLOR = [0, 0, 0]
MOVE_SPEED = 50
ROTATE_DEGRE = 20

import os
import glfw
from control import *
import lib
import time
from tank import *
from bullet import *

tank = Tank(50, 500, 50)
tank2 = Tank(30, 50, 50, 30, 70, (255, 20, 0))
player_1_control = TankControl(tank)
player_2_control = TankControl(tank2)

tank.set_enemy_tank(tank2)
tank2.set_enemy_tank(tank)

def init():
    glClearColor(BACKGROUND_COLOR[0], BACKGROUND_COLOR[1], BACKGROUND_COLOR[2], 0)
    glPointSize(1)
    glMatrixMode(GL_PROJECTION)
    glEnable(GL_LINE_SMOOTH)
    glEnable(GL_POINT_SMOOTH)
    glEnable(GL_VERTEX_PROGRAM_POINT_SIZE)
    glEnable(GL_BLEND)
    glBlendFunc (GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glOrtho(0, WIDTH, 0, HEIGHT, -1, 1)

def read_config_file():
    global WIDTH, HEIGHT, BACKGROUND_COLOR
    file = open(os.path.dirname(__file__)+"/setup.dat", "r")
    for line in file:
        line = line.strip()
        data = line.split('=')
        if data[0] == "WINDOWS_WIDTH":
            WIDTH = int(data[1])
        elif data[0] == "WINDOWS_HEIGHT":
            HEIGHT = int(data[1])
        elif data[0] == "BACKGROUND_COLOR":
            color = data[1].split(',')
            color = lib.convert_rgb_to_float(int(color[0]), int(color[1]), int(color[2]))
            BACKGROUND_COLOR = color

def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # glColor3f(1, 0, 0)
    # glPointSize(10)
    # glBegin(GL_POINTS)
    # glVertex2f(10, 10)
    # glEnd()

    # a =glReadPixels(10, 10,1,1,GL_RGB,GL_FLOAT)
    # print(a[0][0][0], a[1][0][0], a[2][0][0])
    tank.draw()

    for tank1_bullet in tank.list_bullet:
        if tank1_bullet.is_out_map(WIDTH, HEIGHT):
            tank.list_bullet.remove(tank1_bullet)
        else: tank1_bullet.draw()

    tank2.draw()
    for tank2_bullet in tank2.list_bullet:
        if tank2_bullet.is_out_map(WIDTH, HEIGHT):
            tank2.list_bullet.remove(tank2_bullet)
        else: tank2_bullet.draw()
    glFlush()
    
def handle_key(window, key, scancode, action, mods):
    if action != glfw.REPEAT:
    
        # palyer 1 control
        if key == glfw.KEY_W:
            player_1_control.set_move(TOP, action)
        elif key == glfw.KEY_S:
            player_1_control.set_move(BOTTOM, action)
        elif key == glfw.KEY_A:
            player_1_control.set_move(LEFT, action)
        elif key == glfw.KEY_D:
            player_1_control.set_move(RIGHT, action)
        elif key == glfw.KEY_V:
            player_1_control.set_barrel_move(BARREL_LEFT, action)
        elif key == glfw.KEY_B:
            player_1_control.set_barrel_move(BARREL_RIGHT, action)

        # palyer 2 control
        elif key == glfw.KEY_UP:
            player_2_control.set_move(TOP, action)
        elif key == glfw.KEY_DOWN:
            player_2_control.set_move(BOTTOM, action)
        elif key == glfw.KEY_LEFT:
            player_2_control.set_move(LEFT, action)
        elif key == glfw.KEY_RIGHT:
            player_2_control.set_move(RIGHT, action)
        elif key == glfw.KEY_LEFT_BRACKET:
            player_2_control.set_barrel_move(BARREL_LEFT, action)
        elif key == glfw.KEY_RIGHT_BRACKET:
            player_2_control.set_barrel_move(BARREL_RIGHT, action)

def main():
    read_config_file()
    if not glfw.init():
        return
    glfw.window_hint(glfw.RESIZABLE, glfw.FALSE)
    window = glfw.create_window(WIDTH, HEIGHT, "TANK GAME", None, None)
    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)

    glfw.set_key_callback(window, handle_key)
    init()
    
    while not glfw.window_should_close(window):
        draw()
        
        player_1_control.handle_state()
        player_2_control.handle_state()

        # Swap front and back buffers
        glfw.swap_buffers(window)

        # Poll for and process events
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()