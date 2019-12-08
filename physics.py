PAGE_WIDTH = 500
PAGE_HEIGHT = 600
CAR_WIDTH = 40
CAR_HEIGHT = 80
NO_OF_LANES = 2
LANE_MARGIN = 30

STEP_SIZE = 5
ACCELARATION = 20
DECCELERATION = -10
COLLISION_ALLOWANCE = 50
DIR_UP = 0
DIR_DOWN = 1
DIR_LEFT = 2
DIR_RIGHT = 3

RED = (255, 0, 0, 255)
GREEN = (0,255,0, 255)
BLUE = (0, 0, 255, 255)
YELLOW = (255, 255, 0, 255)
BROWN = (150, 75, 0)
WHITE = (150, 75, 0, 255)
TARMAC = (82, 90, 96, 255)
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)


def apply_displacement(v, dt):
    return (v * dt)

def apply_accelaration(u, a, dt):
    return (u + (a * dt))
    