STOP = 0
TOP = 1
BOTTOM = 2
LEFT = 3
RIGHT = 4
TOP_LEFT = 5
TOP_RIGHT = 6
BOTTOM_LEFT = 7
BOTTOM_RIGHT = 8

BARREL_STOP = 10
BARREL_LEFT = 11
BARREL_RIGHT = 12


class TankControl:
    def __init__(self, tank):
        self.top = False
        self.bottom =  False
        self.left =  False
        self.right =  False
        self.barrel_left =  False
        self.barrel_right =  False
        self.tank = tank

    def state(self):
        if self.top and self.left:
            return TOP_LEFT
        elif self.top and self.right:
            return TOP_RIGHT
        elif self.bottom and self.left:
            return BOTTOM_LEFT
        elif self.bottom and self.right:
            return BOTTOM_RIGHT
        elif self.top:
            return TOP
        elif self.bottom:
            return BOTTOM
        elif self.left:
            return LEFT
        elif self.right:
            return RIGHT
        else:
            return STOP
    
    def barrel_state(self):
        if self.barrel_left:
            return BARREL_LEFT
        elif self.barrel_right:
            return BARREL_RIGHT
        else:
            return BARREL_STOP

    def set_move(self, key, action):

        # key release
        if action == 0:
            if key == TOP:
                self.top = False
            elif key == BOTTOM:
                self.bottom = False
            elif key == LEFT:
                self.left = False
            elif key == RIGHT:
                self.right = False
                
        # keypress
        elif action == 1:
            # if key is not pressing => active it
            # if the opposite is pressing => cancel it
            if key == TOP:
                if not self.top: 
                    self.top = True
                if self.bottom:
                    self.bottom = False
            elif key == BOTTOM:
                if not self.bottom: 
                    self.bottom = True
                if self.top:
                    self.top = False
            elif key == LEFT:
                if not self.left: 
                    self.left = True
                if self.right:
                    self.right = False
            elif key == RIGHT:
                if not self.right: 
                    self.right = True
                if self.left: 
                    self.left = False

    def set_barrel_move(self, key, action):
        # key release
        if action == 0:
            if key == BARREL_LEFT:
                self.barrel_left = False
            if key == BARREL_RIGHT:
                self.barrel_right = False
        
        # key press
        elif action == 1:
            if key == BARREL_LEFT:
                if not self.barrel_left: 
                    self.barrel_left = True
                if self.barrel_right:
                    self.barrel_right = False
            if key == BARREL_RIGHT:
                if not self.barrel_right:
                    self.barrel_right = True
                if self.barrel_left: 
                    self.barrel_left = False

    def handle_state(self):
        tank_state = self.state()
        barrel_state = self.barrel_state()

        self.tank.tank_move(tank_state)
        self.tank.barrel_move(barrel_state)
        self.tank.calculate_arg()

