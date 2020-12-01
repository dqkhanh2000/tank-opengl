from OpenGL.GLUT import *
from OpenGL.GL import *

def drawOxy(step_x, step_y):
    glBegin(GL_LINES)
    glVertex2f(0, -HEIGHT)
    glVertex2f(0, HEIGHT)

    glVertex2f(-WIDTH, 0)
    glVertex2f(WIDTH, 0)

    glEnd()
    glPointSize(3)
    glBegin(GL_POINTS)
    for i in range(-WIDTH, WIDTH, step_x):
        glVertex2f(i, 0)

    for i in range(-HEIGHT, HEIGHT, step_y):
        glVertex2f(0, i)

    glEnd()
    glPointSize(POINT_SIZE)

def tranform (point_2d = [], matrix = []):
    """
        This function to transform 2d point with maxtrix(3x3)
    """
    xn = point_2d[0] * matrix[0][0] + point_2d[1] * matrix[1][0] + matrix[2][0]
    yn = point_2d[0] * matrix[0][1] + point_2d[1] * matrix[1][1] + matrix[2][1]
    return [xn, yn]

def convert_rgb_to_float(r, g, b):
    """
    This function used to convert rgb value to float value in range (0, 1)
    return an array
    """
    nr = float("{:.5f}".format(r/255))
    ng = float("{:.5f}".format(g/255))
    nb = float("{:.5f}".format(b/255))
    return [nr, ng, nb]
