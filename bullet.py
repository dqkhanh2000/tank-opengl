class Bullet:
    def __init__(self, name, age):
      self.name = name
      self.age = age

    def drawHexagon(self):
        # glBegin(GL_QUADS)
        # glColor3f(1,0.2,0.2)
        # glVertex3f(0.0, 0.04, 0)
        # glVertex3f(-30, 0.02, 0)
        # glVertex3f(-0.03,-0.02, 0)
        # glVertex3f(0.03, 0.02, 0)
        # glEnd
        # glBegin(GL_QUADS)
        # glColor3f(0.5,0.5,1)
        # glVertex3f(-0.03, -0.02, 0)
        # glVertex3f(0.0, -0.04, 0)
        # glVertex3f(0.03,-0.02, 0)
        # glVertex3f(0.03, 0.02, 0)
        # glEnd
        glColor3f(1,0,1)
        glBegin(GL_POINTS)
        glVertex3fv((12,12,0))
        glEnd()
        glPointSize(4)
