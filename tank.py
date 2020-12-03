from OpenGL.GLUT import *
from OpenGL.GL import *
TANK_WIDTH = 20
TANK_HEIGHT = 20
GUN_WIDTH = TANK_WIDTH
GUN_HEIGHT = TANK_HEIGHT/3

class Tank:
    
    def __init__(self, type, map_width, map_height): 
        self.type = type
        if self.type == 1 :
            self.color = [1, 0.5, 0]
            self.x = map_width/2
            self.y = map_height/2
        else:
            self.color = [0, 0.5, 1]
            self.x = -map_width/2
            self.y = -map_height/2

    def change(self,x,y):
        self.x=x
        self.y=y
    
    def draw_tank(self):
        global TANK_WIDTH, TANK_HEIGHT, GUN_HEIGHT, GUN_WIDTH

        glColor3f (self.color[0], self.color[1], self.color[2]); 
        glBegin(GL_POLYGON)
        glVertex2f(self.x-TANK_WIDTH,self.y+TANK_HEIGHT)
        glVertex2f(self.x+TANK_WIDTH,self.y+TANK_HEIGHT)
        glVertex2f(self.x+TANK_WIDTH,self.y-TANK_HEIGHT)
        glVertex2f(self.x-TANK_WIDTH,self.y-TANK_HEIGHT)
        glEnd()

        glColor3f (0, 0, 0); 
        glLineWidth(5)
        glBegin(GL_LINE_LOOP)
        glVertex2f(self.x-TANK_WIDTH,self.y+TANK_HEIGHT)
        glVertex2f(self.x+TANK_WIDTH,self.y+TANK_HEIGHT)
        glVertex2f(self.x+TANK_WIDTH,self.y-TANK_HEIGHT)
        glVertex2f(self.x-TANK_WIDTH,self.y-TANK_HEIGHT)
        glEnd()
        
        glColor3f (self.color[0], self.color[1], self.color[2]); 
        glBegin(GL_POLYGON)
        glVertex2f(self.x+TANK_WIDTH*3/4,self.y+GUN_HEIGHT)
        glVertex2f(self.x+(TANK_WIDTH*3/4+GUN_WIDTH),self.y+GUN_HEIGHT)
        glVertex2f(self.x+(TANK_WIDTH*3/4+GUN_WIDTH),self.y-GUN_HEIGHT)
        glVertex2f(self.x+TANK_WIDTH*3/4,self.y-GUN_HEIGHT)
        glEnd()

        glColor3f (0, 0, 0); 
        glLineWidth(5)
        glBegin(GL_LINE_LOOP)
        glVertex2f(self.x+TANK_WIDTH*3/4,self.y+GUN_HEIGHT)
        glVertex2f(self.x+(TANK_WIDTH*3/4+GUN_WIDTH),self.y+GUN_HEIGHT)
        glVertex2f(self.x+(TANK_WIDTH*3/4+GUN_WIDTH),self.y-GUN_HEIGHT)
        glVertex2f(self.x+TANK_WIDTH*3/4,self.y-GUN_HEIGHT)
        glEnd()



# def draw_8point(int xc, int yc, int x, int y):
#     glBegin(GL_POINTS);
# 	glVertex2i(xc + x, yc + y);
# 	glVertex2i(xc + y, yc + x);
# 	glVertex2i(xc + y, yc - x);
# 	glVertex2i(xc + x, yc - y);
# 	glVertex2i(xc - x, yc - y);
# 	glVertex2i(xc - y, yc - x);
# 	glVertex2i(xc - y, yc + x);
# 	glVertex2i(xc - x, yc + y);
# 	glEnd();
# def circle_bres(int xc,int yc,int R ):
#     int p ;
# 	int y = R ; 
# 	int x = 0;
# 	p = 3 - 2*R;
# 	draw_8point(xc,yc,x,y);

    
    