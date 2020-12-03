from OpenGL.GLUT import *
from OpenGL.GL import *
class Bullet:
    def __init__(self, coordinates, direction):
      self.coordinates = coordinates
      self.direction = direction
      self.withB = 8
      self.heightB = 8

    def drawBullet(self):
        changeCoordinates(self)
        glColor3f(1,0,1)
        glBegin(GL_POINTS)
        glVertex3fv((self.coordinates[0],self.coordinates[1],0))
        glEnd()
        glPointSize(4)
    def changeCoordinates():
        coordinates[0]=coordinates[0]+direction[0]
        coordinates[1]=coordinates[1]+direction[1]
        