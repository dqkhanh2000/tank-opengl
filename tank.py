from lib import *
from math import pi, sin, cos


class Tank:
    def __init__(self, x, y, tank_size, tank_direction = 0, barrel_direction = 0, tank_color = (50, 120, 170), border_size = 3):
        self.x = x
        self.y = y
        self.tank_size = tank_size
        self.tank_direction = tank_direction
        self.barrel_direction = barrel_direction
        self.tank_color = tank_color
        self.border_size = border_size
        self.calculate_arg()

    def init_arg(self):
        size = int(self.tank_size / 2)
        border_size = int(size/3)
        self.barrel_radius = size-border_size
        barrel_height = int(size/5)

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
            [(self.barrel_radius+size), barrel_height],
            [(self.barrel_radius - barrel_height), barrel_height],
            [(self.barrel_radius - barrel_height), -barrel_height],
            [(self.barrel_radius+size), -barrel_height]
        ]
        
    def calculate_arg(self):
        self.init_arg()
        rad_tank = self.tank_direction * (pi/180)
        rad_barrel = self.barrel_direction * (pi/180)
        rotate_tank = [
            [cos(rad_tank), sin(rad_tank), 0],
            [-sin(rad_tank), cos(rad_tank), 0],
            [0, 0, 1]
        ]

        move_matrix = [
            [1, 0, 0],
            [0, 1, 0],
            [self.x, self.y, 0]
        ]

        rotate_barrel = [
            [cos(rad_barrel), sin(rad_barrel), 0],
            [-sin(rad_barrel), cos(rad_barrel), 0],
            [0, 0, 1]
        ]
        
        self.points_body = tranform_points(self.points_body, rotate_tank)
        self.points_body = tranform_points(self.points_body, move_matrix)

        self.points_border_bottom_left = tranform_points(self.points_border_bottom_left, rotate_tank)
        self.points_border_bottom_left = tranform_points(self.points_border_bottom_left, move_matrix)

        self.points_border_bottom_right = tranform_points(self.points_border_bottom_right, rotate_tank)
        self.points_border_bottom_right = tranform_points(self.points_border_bottom_right, move_matrix)

        self.points_border_top_left = tranform_points(self.points_border_top_left, rotate_tank)
        self.points_border_top_left = tranform_points(self.points_border_top_left, move_matrix)

        self.points_border_top_right = tranform_points(self.points_border_top_right, rotate_tank)
        self.points_border_top_right = tranform_points(self.points_border_top_right, move_matrix)

        self.points_barrel = tranform_points(self.points_barrel, rotate_barrel)
        self.points_barrel = tranform_points(self.points_barrel, move_matrix)

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


        
