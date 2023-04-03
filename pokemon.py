#POKEMON CLASS FILE

import math
import random
class Pokemon():

    def __init__(self, stats, lv=50):
        self.name = stats[1]
        self.lv = lv
        self.types = stats[2].split(';')
        self.health = math.floor((int(stats[3]))/100 + self.lv + 10)
        self.attack = math.floor((int(stats[4]))/100 + 5)
        self.defense = math.floor((int(stats[5])) / 100 + 5)
        self.spattack = math.floor((int(stats[6])) / 100 + 5)
        self.spdefense = math.floor((int(stats[7])) / 100 + 5)
        self.speed = math.floor((int(stats[8])) / 100 + 5)
        self.evasion = 100
        self.moveset = stats[9].split(';')
        self.actual_moves = self.moveset[:4]
        self.start_status = {}
        self.end_status = {}
        self.picture = ''

    def __str__(self):
        return str(self.name + '\n' + ';'.join(self.types) + '\n' + ';'.join(self.actual_moves))

    def choose_moves(self):
        self.actual_moves = random.sample(self.moveset, 4)

