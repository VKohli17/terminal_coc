import numpy
import json

def distance(x1, y1, x2, y2):
    return numpy.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def get_config():
    config = {
    "king_damage": 100,
    "king_hp": 1000,
    "king_speed": 1,
    "king_aoe": 4,
    "cannon_damage": 25,
    "cannon_hp": 300,
    "cannon_range": 7,
    "barb_damage": 50,
    "barb_hp": 80,
    "barb_speed": 1,
    "arch_range": 8,
    "queen_range": 8,
    "queen_damage": 80,
    "queen_hp": 500,
    "queen_aoe": 3,
    "queen_speed": 1,
    "eagle_aoe": 5,
    "eagle_range": 16,
    "hut_hp": 120,
    "th_hp": 600,
    "wall_hp": 700
    }
    return config