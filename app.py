import os
from OpenGL.GL import *
import glfw
import lib
import bullet
import time

WIDTH = 500
HEIGHT = 500
BACKGROUND_COLOR = [0, 0, 0]
pressing_key_1 = None
pressing_key_2 = None
bu = bullet.Bullet([10,10],[2,2])
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
    
    bu.changeCoordinates()
    bu.drawBullet()
    # lib.drawOxy(WIDTH, HEIGHT, 100, 100, 4)
    glFlush()
    time.sleep(0.1)
    
    
    

def handle_key(window, key, scancode, action, mods):

    if action == glfw.PRESS:
        if pressing_key_1 is not None and pressing_key_2 is not None:
            pass
        elif pressing_key_1 is None and pressing_key_2 is not None:
            pass
            



    
    # if key == glfw.KEY_W and action == glfw.PRESS:
    #     key_pressed()

    # elif key == glfw.KEY_W and action == glfw.REPEAT:
    #     key_W_pressed()

    # elif key == glfw.KEY_A and action == glfw.REPEAT:
    #     key_W_pressed()
    

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

        # Swap front and back buffers
        glfw.swap_buffers(window)

        # Poll for and process events
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()