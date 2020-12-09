from lib import *

def drawW(x,y,s):
    W_map = ((30*s+x,30*s+y,0),(15*s+x,-30*s+y,0),(0*s+x,30*s+y,0),(-15*s+x,-30*s+y,0),(-30*s+x,30*s+y,0))
    glPointSize(11)
    glColor3f(0,0,0)
    glBegin(GL_POINTS)
    for point in W_map:
        glVertex3fv(point)
    glEnd()

    glLineWidth(8)

    glBegin(GL_LINES)
    for item in range(4):
        glVertex3fv(W_map[item])
        if item != 4 :
            glVertex3fv(W_map[item+1])
    glEnd()

def drawI(x,y,s):
    I_map = ((-20*s+x,30*s+y,0),(20*s+x,30*s+y,0),(0*s+x,30*s+y,0),(0*s+x,-30*s+y,0),(-20*s+x,-30*s+y,0),(20*s+x,-30*s+y,0))
    edges = (
        (0,1),
        (2,3),
        (4,5)
    )
    glPointSize(10)
    glColor3f(0,0,0)
    glBegin(GL_POINTS)
    for point in I_map:
        glVertex3fv(point)
    glEnd()

    glLineWidth(8)

    glBegin(GL_LINES)
    for item in edges:
        for it in item:
            glVertex3fv(I_map[it])
        
    glEnd()

def drawN(x,y,s):
    N_map = ((-25*s+x,-30*s+y,0),(-25*s+x,30*s+y,0),(25*s+x,-30*s+y,0),(25*s+x,30*s+y,0))
    edges = ((0,1),(1,2),(2,3))
    glPointSize(10)
    glColor3f(0,0,0)
    glBegin(GL_POINTS)
    for point in N_map:
        glVertex3fv(point)
    glEnd()

    glLineWidth(8)

    glBegin(GL_LINES)
    for item in edges:
        for it in item:
            glVertex3fv(N_map[it])  
    glEnd()

def draw_num_1(x,y,s):
    one_map = ((-20*s+x,20*s+y,0),(0*s+x,25*s+y,0),(0*s+x,30*s+y,0),(0*s+x,-30*s+y,0),(-20*s+x,-30*s+y,0),(20*s+x,-30*s+y,0))
    edges = ((0,1),(2,3),(4,5))
    glPointSize(10)
    glColor3f(0,0,0)
    glBegin(GL_POINTS)
    for point in one_map:
        glVertex3fv(point)
    glEnd()

    glLineWidth(8)

    glBegin(GL_LINES)
    for item in edges:
        for it in item:
            glVertex3fv(one_map[it])  
    glEnd()

def draw_num_2(x,y,s):
    two_map = ((-20*s+x,20*s+y,0),(-10*s+x,30*s+y,0),(10*s+x,30*s+y,0),(20*s+x,25*s+y,0),(30*s+x,10*s+y,0),(-30*s+x,-30*s+y,0),(30*s+x,-30*s+y,0))
    edges = ((0,1),(1,2),(2,3),(3,4),(4,5),(5,6))
    glPointSize(5)
    glColor3f(0,0,0)
    glBegin(GL_POINTS)
    for point in two_map:
        glVertex3fv(point)
    glEnd()

    glLineWidth(7)

    glBegin(GL_LINES)
    for item in edges:
        for it in item:
            glVertex3fv(two_map[it])  
    glEnd()