import os
from OpenGL.GL import *
import glfw
from control import *
import lib
import bullet
import time

WIDTH = 500
HEIGHT = 500
BACKGROUND_COLOR = [0, 0, 0]
player_1_control = TankControl()
player_2_control = TankControl()

def init():
    glClearColor(BACKGROUND_COLOR[0], BACKGROUND_COLOR[1], BACKGROUND_COLOR[2], 0)
    glPointSize(1)
    glMatrixMode(GL_PROJECTION)
    glOrtho(-WIDTH, WIDTH, -HEIGHT, HEIGHT, -1, 1)
    # glViewport(0, 0, WIDTH, HEIGHT)

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
    
    glFlush()
    time.sleep(0.1)
    
    
    

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
            player_1_control.set_move(BARREL_LEFT, action)
        elif key == glfw.KEY_B:
            player_1_control.set_move(BARREL_RIGHT, action)

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
            player_2_control.set_move(BARREL_LEFT, action)
        elif key == glfw.KEY_RIGHT_BRACKET:
            player_2_control.set_move(BARREL_RIGHT, action)

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

        state_player_1 = player_1_control.state()
        state_player_2 = player_2_control.state()
        # Swap front and back buffers
        glfw.swap_buffers(window)

        # Poll for and process events
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()