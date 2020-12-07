from lib import *

class Bullet:
    def __init__(self, x, y, direction, color = (50, 120, 170), size = 7, border_size = 3, speed = 4):
        self.x = x
        self.y = y
        self.direction = direction
        self.size = size
        self.color = color
        self.border_size = border_size
        
        rad = self.direction * (pi/180)
        matrix_direction = [
            [cos(rad), sin(rad), 0],
            [-sin(rad), cos(rad), 0],
            [0, 0, 1]
        ]
        x_direction, y_direction = tranform([speed, 0], matrix_direction)
        self.matrix_move = [
            [1, 0, 0],
            [0, 1, 0],
            [int(x_direction), int(y_direction), 0]
        ]

    def draw(self):
        glColor3ubv(self.color)
        glBegin(GL_POLYGON)
        draw_circle(self.x, self.y, self.size)
        glEnd()

        glColor3f(0, 0, 0)
        glPointSize(self.border_size)
        glBegin(GL_POINTS)
        draw_circle(self.x, self.y, self.size)
        glEnd()
        self.calculate_next_cordinate()

    def calculate_next_cordinate(self):
        self.x, self.y = tranform([self.x, self.y], self.matrix_move)

    def is_out_map(self, map_width, map_height):
        if abs(self.x) > map_width + self.size or abs(self.y) > map_height + self.size:
            return True
        return False