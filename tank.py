from bullet import Bullet
from lib import *
from control import *

ROTATE_DEGRE = 3
MOVE_SPEED = 2
MAP_WIDTH = 480 - 50
MAP_HEIGHT = 640 - 50


class Tank:
    def __init__(self, x, y, tank_size, tank_direction = 0, barrel_direction = 0, tank_color = (50, 120, 170), border_size = 3):
        self.x = x
        self.y = y
        self.tank_size = tank_size
        self.tank_direction = tank_direction
        self.barrel_direction = barrel_direction
        self.tank_color = tank_color
        self.border_size = border_size
        self.list_bullet = []
        self.calculate_arg()
        self.count_repeat = 0;

    def init_arg(self):
        size = int(self.tank_size / 2)
        border_size = int(size/3)
        self.barrel_radius = size-border_size
        self.barrel_height = int(size/5)
        self.barrel_position = self.barrel_radius + size - self.barrel_height

        self.points_body =[
            [-(size-border_size), -size],
            [(size-border_size), -size],
            [size, -(size-border_size)],
            [size, (size-border_size)],
            [(size-border_size), size],
            [-(size-border_size), size],
            [-size, (size-border_size)],
            [-size, -(size-border_size)],
        ]

        self.points_border_bottom_left = [
            [-(size-border_size), -size],
            [-size, -size],
            [-size, -(size-border_size)]
        ]

        self.points_border_bottom_right = [
            [(size-border_size), -size],
            [size, -size],
            [size, -(size-border_size)]
        ]

        self.points_border_top_right = [
            [(size-border_size), size],
            [size, size],
            [size, (size-border_size)]
        ]

        self.points_border_top_left = [
            [-(size-border_size), size],
            [-size, size],
            [-size, (size-border_size)]
        ]

        self.points_barrel = [
            [self.barrel_position, self.barrel_height],
            [(self.barrel_radius - self.barrel_height), self.barrel_height],
            [(self.barrel_radius - self.barrel_height), - self.barrel_height],
            [(self.barrel_position), - self.barrel_height]
        ]
        
    def calculate_arg(self):
        self.init_arg()
        rad_tank = self.tank_direction * (pi/180)
        rad_barrel = self.barrel_direction * (pi/180)
        matrix_move_tank = [
            [cos(rad_tank), sin(rad_tank), 0],
            [-sin(rad_tank), cos(rad_tank), 0],
            [self.x, self.y, 1]
        ]

        matrix_move_barrel = [
            [cos(rad_barrel), sin(rad_barrel), 0],
            [-sin(rad_barrel), cos(rad_barrel), 0],
            [self.x, self.y, 1]
        ]
        
        self.points_body = tranform_points(self.points_body, matrix_move_tank)

        self.points_border_bottom_left = tranform_points(self.points_border_bottom_left, matrix_move_tank)

        self.points_border_bottom_right = tranform_points(self.points_border_bottom_right, matrix_move_tank)

        self.points_border_top_left = tranform_points(self.points_border_top_left, matrix_move_tank)

        self.points_border_top_right = tranform_points(self.points_border_top_right, matrix_move_tank)

        self.points_barrel = tranform_points(self.points_barrel, matrix_move_barrel)

    def draw(self):
        # draw tank body
            # draw backgound tank body
        glLineWidth(self.border_size)
        glColor3ubv(self.tank_color)
        glBegin(GL_POLYGON)
        draw_points(self.points_body)
        draw_bezier(self.points_border_bottom_left)
        draw_bezier(self.points_border_bottom_right)
        draw_bezier(self.points_border_top_left)
        draw_bezier(self.points_border_top_right)
        glEnd()

        # draw border body
        glColor3f(0, 0, 0)
        glLineWidth(self.border_size)
        glBegin(GL_LINES)
        draw_points(self.points_body)
        glEnd()

        glBegin(GL_LINE_STRIP)
        draw_bezier(self.points_border_bottom_left)
        glEnd()

        glBegin(GL_LINE_STRIP)
        draw_bezier(self.points_border_bottom_right)
        glEnd()

        glBegin(GL_LINE_STRIP)
        draw_bezier(self.points_border_top_left)
        glEnd()

        glBegin(GL_LINE_STRIP)
        draw_bezier(self.points_border_top_right)
        glEnd()

        # draw barrel
        # draw background barrel
        glColor3ubv(self.tank_color)
        glBegin(GL_POLYGON)
        draw_points(self.points_barrel)
        glEnd()

        # draw border barrel
        glColor3f(0, 0,  0)
        glLineWidth(self.border_size)
        glBegin(GL_LINE_LOOP)
        draw_points(self.points_barrel)
        glEnd()

        # draw circle
        # background
        glColor3ubv(self.tank_color)
        glBegin(GL_POLYGON)
        draw_circle(self.x, self.y, self.barrel_radius)
        glEnd()

        # border
        glColor3f(0, 0, 0)
        glPointSize(self.border_size)
        glBegin(GL_POINTS)
        draw_circle(self.x, self.y, self.barrel_radius)
        glEnd()

    def set_enemy_tank(self, enemy):
        self.enemy = enemy

    def tank_move(self, state):
        if state == TOP:
            if self.tank_direction < 90:
                self.tank_direction += ROTATE_DEGRE
            elif self.tank_direction > 90:
                self.tank_direction -= ROTATE_DEGRE
            if self.y < MAP_HEIGHT + self.tank_size/2 - self.border_size:
                t1 = abs(self.y + MOVE_SPEED - self.enemy.y)
                t2 = abs(self.x - self.enemy.x)

                if t1 > -self.tank_size and t1 < self.tank_size and t1 > -self.tank_size and t2 < self.tank_size:
                    if self.enemy.y < MAP_HEIGHT + self.tank_size/2 - self.border_size:
                        self.y += 2
                        self.enemy.y +=2
                else :
                    self.y += MOVE_SPEED

        elif state == BOTTOM:
            if self.tank_direction < 90:
                self.tank_direction += ROTATE_DEGRE
            elif self.tank_direction > 90:
                self.tank_direction -= ROTATE_DEGRE
            if self.y > 0 + self.tank_size/2 + self.border_size:
                t1 = abs(self.y - MOVE_SPEED*2 - self.enemy.y)
                t2 = abs(self.x - self.enemy.x)

                if t1 > -self.tank_size and t1 < self.tank_size and t1 > -self.tank_size and t2 < self.tank_size:
                    if self.enemy.y > 0 + self.tank_size/2 + self.border_size:
                        self.y -= 2
                        self.enemy.y -= 2
                else :
                    self.y -= MOVE_SPEED

        elif state == LEFT:
            if self.tank_direction < 90:
                self.tank_direction += ROTATE_DEGRE
            elif self.tank_direction > 90:
                self.tank_direction -= ROTATE_DEGRE
            if self.x > self.tank_size/2 + self.border_size:
                t1 = abs(self.y - self.enemy.y)
                t2 = abs(self.x - MOVE_SPEED*2 - self.enemy.x)

                if t1 > -self.tank_size and t1 < self.tank_size and t1 > -self.tank_size and t2 < self.tank_size:
                    if self.enemy.x > self.tank_size/2 + self.border_size:
                        self.x -= 2
                        self.enemy.x -= 2
                else :
                    self.x -= MOVE_SPEED

        elif state == RIGHT:
            if self.tank_direction < 90:
                self.tank_direction += ROTATE_DEGRE
            elif self.tank_direction > 90:
                self.tank_direction -= ROTATE_DEGRE
            if self.x < MAP_WIDTH + self.tank_size/2 - self.border_size:
                t1 = abs(self.y - self.enemy.y)
                t2 = abs(self.x + MOVE_SPEED*2 - self.enemy.x)

                if t1 > -self.tank_size and t1 < self.tank_size and t1 > -self.tank_size and t2 < self.tank_size:
                    if self.enemy.x < MAP_WIDTH + self.tank_size/2 - self.border_size:
                        self.x += 2
                        self.enemy.x += 2
                else :
                    self.x += MOVE_SPEED

        elif state == TOP_LEFT:
            if self.tank_direction < 135:
                self.tank_direction += ROTATE_DEGRE
            elif self.tank_direction > 135:
                self.tank_direction -= ROTATE_DEGRE
            if self.x > self.tank_size/2 + self.border_size:
                t1 = abs(self.y - self.enemy.y)
                t2 = abs(self.x - MOVE_SPEED*2 - self.enemy.x)

                if t1 > -self.tank_size and t1 < self.tank_size and t1 > -self.tank_size and t2 < self.tank_size:
                    if self.enemy.x > self.tank_size/2 + self.border_size:
                        self.x -= 2
                        self.enemy.x -= 2
                else :
                    self.x -= MOVE_SPEED
            if self.y < MAP_HEIGHT - self.tank_size/2 - self.border_size:
                t1 = abs(self.y + MOVE_SPEED - self.enemy.y)
                t2 = abs(self.x - self.enemy.x)

                if t1 > -self.tank_size and t1 < self.tank_size and t1 > -self.tank_size and t2 < self.tank_size:
                    if self.enemy.y < MAP_HEIGHT + self.tank_size/2 - self.border_size:
                        self.y += 2
                        self.enemy.y +=2
                else :
                    self.y += MOVE_SPEED

        elif state == TOP_RIGHT:
            if self.tank_direction < 45:
                self.tank_direction += ROTATE_DEGRE
            elif self.tank_direction > 45:
                self.tank_direction -= ROTATE_DEGRE
            if self.x < MAP_WIDTH - self.tank_size/2 - self.border_size:
                t1 = abs(self.y - self.enemy.y)
                t2 = abs(self.x + MOVE_SPEED*2 - self.enemy.x)

                if t1 > -self.tank_size and t1 < self.tank_size and t1 > -self.tank_size and t2 < self.tank_size:
                    if self.enemy.x < MAP_WIDTH + self.tank_size/2 - self.border_size:
                        self.x += 2
                        self.enemy.x += 2
                else :
                    self.x += MOVE_SPEED
            if self.y < MAP_HEIGHT - self.tank_size/2 - self.border_size:
                t1 = abs(self.y + MOVE_SPEED - self.enemy.y)
                t2 = abs(self.x - self.enemy.x)

                if t1 > -self.tank_size and t1 < self.tank_size and t1 > -self.tank_size and t2 < self.tank_size:
                    if self.enemy.y < MAP_HEIGHT + self.tank_size/2 - self.border_size:
                        self.y += 2
                        self.enemy.y +=2
                else :
                    self.y += MOVE_SPEED

        elif state == BOTTOM_LEFT:
            if self.tank_direction < 45:
                    self.tank_direction += ROTATE_DEGRE
            elif self.tank_direction > 45:
                self.tank_direction -= ROTATE_DEGRE
            if self.x > self.tank_size/2 + self.border_size:
                t1 = abs(self.y - self.enemy.y)
                t2 = abs(self.x - MOVE_SPEED*2 - self.enemy.x)

                if t1 > -self.tank_size and t1 < self.tank_size and t1 > -self.tank_size and t2 < self.tank_size:
                    if self.enemy.x > self.tank_size/2 + self.border_size:
                        self.x -= 2
                        self.enemy.x -= 2
                else :
                    self.x -= MOVE_SPEED
            if self.y > self.tank_size/2 + self.border_size:
                t1 = abs(self.y - MOVE_SPEED*2 - self.enemy.y)
                t2 = abs(self.x - self.enemy.x)

                if t1 > -self.tank_size and t1 < self.tank_size and t1 > -self.tank_size and t2 < self.tank_size:
                    if self.enemy.y > 0 + self.tank_size/2 + self.border_size:
                        self.y -= 2
                        self.enemy.y -= 2
                else :
                    self.y -= MOVE_SPEED
        elif state == BOTTOM_RIGHT:
            if self.tank_direction < 135:
                    self.tank_direction += ROTATE_DEGRE
            elif self.tank_direction > 135:
                self.tank_direction -= ROTATE_DEGRE
            if self.x < MAP_WIDTH - self.tank_size/2 - self.border_size:
                t1 = abs(self.y - self.enemy.y)
                t2 = abs(self.x + MOVE_SPEED*2 - self.enemy.x)

                if t1 > -self.tank_size and t1 < self.tank_size and t1 > -self.tank_size and t2 < self.tank_size:
                    if self.enemy.x < MAP_WIDTH + self.tank_size/2 - self.border_size:
                        self.x += 2
                        self.enemy.x += 2
                else :
                    self.x += MOVE_SPEED
            if self.y > self.tank_size/2 + self.border_size:
                t1 = abs(self.y - MOVE_SPEED*2 - self.enemy.y)
                t2 = abs(self.x - self.enemy.x)

                if t1 > -self.tank_size and t1 < self.tank_size and t1 > -self.tank_size and t2 < self.tank_size:
                    if self.enemy.y > 0 + self.tank_size/2 + self.border_size:
                        self.y -= 2
                        self.enemy.y -= 2
                else :
                    self.y -= MOVE_SPEED

    def barrel_move(self, state):
        if self.count_repeat > 10:
            new_bullet = Bullet(self.points_barrel[0][0], self.points_barrel[0][1], self.barrel_direction, self.tank_color)
            self.list_bullet.append(new_bullet)
            self.count_repeat = 0

        if state == BARREL_LEFT:
            self.barrel_direction += ROTATE_DEGRE
            self.count_repeat +=1
        elif state == BARREL_RIGHT:
            self.barrel_direction -= ROTATE_DEGRE
            self.count_repeat +=1

        if self.barrel_direction >= 360:
            self.barrel_direction = 360 - self.barrel_direction
