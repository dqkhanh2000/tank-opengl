from OpenGL.GL import *
from math import pi, sin, cos, factorial, pow

def drawOxy(x, y, step_x, step_y, point_size):
    glLineWidth(1)
    glBegin(GL_LINES)
    glVertex2f(0, -y)
    glVertex2f(0, y)

    glVertex2f(-x, 0)
    glVertex2f(x, 0)

    glEnd()
    glPointSize(point_size)
    glBegin(GL_POINTS)
    for i in range(0, x, step_x):
        glVertex2f(i, 0)
        glVertex2f(-i, 0)

    for i in range(0, y, step_y):
        glVertex2f(0, i)
        glVertex2f(0, -i)

    glEnd()

def tranform (point_2d = [], matrix = []):
    """
        This function to transform 2d point with maxtrix(3x3)
    """
    xn = point_2d[0] * matrix[0][0] + point_2d[1] * matrix[1][0] + matrix[2][0]
    yn = point_2d[0] * matrix[0][1] + point_2d[1] * matrix[1][1] + matrix[2][1]
    return [xn, yn]

def tranform_points(points = [], matrix = []):
    results = []
    for point in points:
        results.append(tranform(point, matrix))
    return results

def convert_rgb_to_float(r, g, b):
    """
    This function used to convert rgb value to float value in range (0, 1)
    return an array
    """
    nr = float("{:.5f}".format(r/255))
    ng = float("{:.5f}".format(g/255))
    nb = float("{:.5f}".format(b/255))
    return [nr, ng, nb]

def __bern_stein(t, n, k):
    ckn = factorial(n) / ( factorial(k) * factorial(n - k) )
    kq = ckn * pow(1 - t, n - k) * pow(t, k)
    return kq

def __point_t_bezier(points, t):
    n = len(points)
    point_t = [0 ,0]
    for k in range(0, n):	
        B = __bern_stein(t, n-1, k)
        point_t[0] += points[k][0] * B
        point_t[1] += points[k][1] * B
    return point_t

def draw_bezier(points = []): 
    """just include glVertex2f, must insert glBegin and glEnd

    Args:
        points (list, optional): [description]. Defaults to [].
    """
    point_t = []
    t=0
    m=5
    dt= 1/m 
    glVertex2f(points[0][0], points[0][1])
    for i in range(0, m+1):      
        point_t = __point_t_bezier(points,t)
        glVertex2f(point_t[0], point_t[1])
        t+=dt

def __draw8point(xc, yc, x, y):
    glVertex2f(xc + x, yc + y)
    glVertex2f(xc + y, yc + x)
    glVertex2f(xc + y, yc - x)
    glVertex2f(xc + x, yc - y)
    glVertex2f(xc - x, yc - y)
    glVertex2f(xc - y, yc - x)
    glVertex2f(xc - y, yc + x)
    glVertex2f(xc - x, yc + y)

def draw_circle(xc, yc, r):
    """just include glVertex2f, must insert glBegin and glEnd

    Args:
        xc (int): x value of center
        yc (int): y value of center
        r (int): radius of circle
    """
    y = r  
    x = 0
    p = 3 - 2*r
    __draw8point(xc,yc,x,y)
    while (x < y):
        if (p <0): 
            p +=4*x+6
        else:
            p += 4*(x-y)+10
            y-=1
        x+=1
        __draw8point(xc,yc,x,y)

def draw_points(points = []):
    """just include glVertex2f, must insert glBegin and glEnd

    Args:
        points (list, optional): [description]. Defaults to [].
    """
    for i in range(0, len(points)):
        glVertex2f(points[i][0], points[i][1])