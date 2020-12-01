
from OpenGL.GLUT import *
from OpenGL.GL import *
import lib

WIDTH = 500
HEIGHT = 500
BACKGROUND_COLOR = [0, 0, 0]

def init():
    glClearColor(BACKGROUND_COLOR[0], BACKGROUND_COLOR[1], BACKGROUND_COLOR[2], 0)
    glPointSize(4.0)
    glMatrixMode(GL_PROJECTION)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glOrtho(-WIDTH, WIDTH, -HEIGHT, HEIGHT, -1, 1)

def read_config_file():
    global WIDTH, HEIGHT, BACKGROUND_COLOR
    file = open("setup.dat", "r")
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
    # lib.drawOxy(10, 10)
    glFlush()

def main():
    read_config_file()
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Bien doi 2d")
    glutDisplayFunc(draw)
    init()
    glutMainLoop()

if __name__ == "__main__":
    main()