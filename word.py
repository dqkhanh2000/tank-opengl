from lib import *


class Word:
    def __init__(self, x, y,word_size):
        self.x = x
        self.y = y
        self.color= (0, 0, 0)
        self.line_size=5
        self.word_size=word_size
        self.points =[
            [75/self.word_size + self.x, 395/self.word_size + self.y],
            [100/self.word_size + self.x, 395/self.word_size + self.y],
            [100/self.word_size + self.x, 350/self.word_size + self.y],
            [75/self.word_size + self.x, 350/self.word_size + self.y]
        ]
        self.points_2=[
            [380/self.word_size + self.x, 395/self.word_size + self.y],
            [405/self.word_size + self.x, 395/self.word_size + self.y],
            [405/self.word_size + self.x, 350/self.word_size + self.y],
            [380/self.word_size + self.x, 350/self.word_size + self.y]
        ]
    def draw_word(self):
        glColor3ubv(self.color)
        glLineWidth(5)
        glBegin(GL_LINE_STRIP)
        glVertex2f(75/self.word_size + self.x,  395/self.word_size + self.y)
        glVertex2f(50/self.word_size + self.x,  395/self.word_size + self.y)
        glVertex2f(50/self.word_size + self.x,  300/self.word_size + self.y)
        glEnd()
        glBegin(GL_LINE_STRIP)
        draw_bezier(self.points)
        glEnd()
        glBegin(GL_LINES)
        glVertex2f(50/self.word_size + self.x,  350/self.word_size + self.y)
        glVertex2f(75/self.word_size + self.x,  350/self.word_size + self.y)
        glEnd()

        glBegin(GL_LINE_STRIP)
        glVertex2f(110/self.word_size + self.x,  400/self.word_size + self.y)
        glVertex2f(110/self.word_size + self.x,  305/self.word_size + self.y)
        glVertex2f(145/self.word_size + self.x,  305/self.word_size + self.y)
        glEnd()

        glBegin(GL_LINE_STRIP)
        glVertex2f(165/self.word_size + self.x,  300/self.word_size + self.y)
        glVertex2f(190/self.word_size + self.x,  400/self.word_size + self.y)
        glVertex2f(215/self.word_size + self.x,  300/self.word_size + self.y)
        glEnd()
        glBegin(GL_LINES)
        glVertex2f(171/self.word_size + self.x,  335/self.word_size + self.y)
        glVertex2f(209/self.word_size + self.x,  335/self.word_size + self.y)
        glEnd()

        glBegin(GL_LINE_STRIP)
        glVertex2f(225/self.word_size + self.x,  400/self.word_size + self.y)
        glVertex2f(250/self.word_size + self.x,  350/self.word_size + self.y)
        glVertex2f(275/self.word_size + self.x,  400/self.word_size + self.y)
        glEnd()
        glBegin(GL_LINES)
        glVertex2f(250/self.word_size + self.x,  350/self.word_size + self.y)
        glVertex2f(250/self.word_size + self.x,  300/self.word_size + self.y)
        glEnd()

        glBegin(GL_LINE_STRIP)
        glVertex2f(335/self.word_size + self.x,  305/self.word_size + self.y)
        glVertex2f(295/self.word_size + self.x, 305/self.word_size + self.y)
        glVertex2f(295/self.word_size + self.x,  395/self.word_size + self.y)
        glVertex2f(335/self.word_size + self.x,  395/self.word_size + self.y)
        glEnd()
        glBegin(GL_LINES)
        glVertex2f(295/self.word_size + self.x,  350/self.word_size + self.y)
        glVertex2f(335/self.word_size + self.x,  350/self.word_size + self.y)
        glEnd()

        glBegin(GL_LINE_STRIP)
        glVertex2f(380/self.word_size + self.x,  395/self.word_size + self.y)
        glVertex2f(355/self.word_size + self.x,  395/self.word_size + self.y)
        glVertex2f(355/self.word_size + self.x,  300/self.word_size + self.y)
        glEnd()
        glBegin(GL_LINE_STRIP)
        draw_bezier(self.points_2)
        glEnd()
        glBegin(GL_LINES)
        glVertex2f(355/self.word_size + self.x,  350/self.word_size + self.y)
        glVertex2f(380/self.word_size + self.x,  350/self.word_size + self.y)
        glEnd()
        glBegin(GL_LINES)
        glVertex2f(400/self.word_size + self.x,  300/self.word_size + self.y)
        glVertex2f(375/self.word_size + self.x,  350/self.word_size + self.y)
        glEnd()
      


        