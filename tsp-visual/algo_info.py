from util import *
from algo import BruteForce

ALGO_INFO = [
    {
        "name": "Genetic Algo",
        "displacement": (0, FONT_HEIGHT),
        "name_coords": (0, 0),
        "length_coords": (0, HEIGHT + FONT_HEIGHT),
        "depends" : -1,
        "sim" : BruteForce.BruteForceSolver
    },
]

DIVIDERS = [
    (0, HEIGHT + FONT_HEIGHT, WINDOW_WIDTH, HEIGHT + FONT_HEIGHT),
    (WIDTH, 0, WIDTH, WINDOW_HEIGHT),
    (WIDTH, 0, WIDTH, WINDOW_HEIGHT),
    (WIDTH, 0, WIDTH, WINDOW_HEIGHT),
]