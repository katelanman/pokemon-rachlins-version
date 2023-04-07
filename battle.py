# Creating a battle
from Pokemon import Pokemon
import random


class Battle():

    def __init__(self, poke1, poke2):
        self.poke1 = poke1
        self.poke2 = poke2

    def round(self, poke1_move, poke2_move):

        # check start statuses
        # Pokemon 1
        if "Burn" in self.poke1.start_status.keys():
            self.poke1.attack = self.poke1.attack / 2

        if "Paralyze" in self.poke1.start_status.keys():
            self.poke1.speed = self.poke1.speed / 4
            if random.random() < .25:
                poke1_move = "Paralyzed"

        if "Sleep" in self.poke1.start_status.keys():
            if self.poke1.start_status["Sleep"]["turns"] > 0:
                self.poke1.start_status["Sleep"]["turns"] -= 1
                poke1_move = "Asleep"

        if "Freeze" in self.poke1.start_status.keys():
            if random.random() < .2:
                del self.poke1.start_status["Freeze"]
            else:
                poke1_move = "Frozen"

        if "Confuse" in self.poke1.start_status.keys():
            if self.poke1.start_status["Confuse"]["turns"] > 0:
                self.poke1.start_status["Confuse"]["turns"] -= 1
            if random.random() < .5:
                poke1_move = "Confused"

        # Needs fixed
        if "Delayed" in self.poke1.start_status.keys():
            poke1_next_move = self.poke1.start_status["Delayed"]
            poke1_move = "Delayed"
            del self.poke1.start_status["Delayed"]

        if "Flinch" in self.poke1.start_status.keys():
            if self.poke1.speed < self.poke2.speed:
                poke1_move = "Flinched"

        # Pokemon 2
        if "Burn" in self.poke2.start_status.keys():
            self.poke2.attack = self.poke2.attack / 2

        if "Paralyze" in self.poke2.start_status.keys():
            self.poke2.speed = self.poke2.speed / 4
            if random.random() < .25:
                poke2_move = "Paralyzed"

        if "Sleep" in self.poke2.start_status.keys():
            if self.poke2.start_status["Sleep"]["turns"] > 0:
                self.poke2.start_status["Sleep"]["turns"] -= 1
                poke2_move = "Asleep"

        if "Freeze" in self.poke2.start_status.keys():
            if random.random() < .2:
                del self.poke2.start_status["Freeze"]
            else:
                poke2_move = "Frozen"

        if "Confuse" in self.poke2.start_status.keys():
            if self.poke2.start_status["Confuse"]["turns"] > 0:
                self.poke2.start_status["Confuse"]["turns"] -= 1
            if random.random() < .5:
                poke2_move = "Confused"

        # Needs fixed
        if "Delayed" in self.poke2.start_status.keys():
            poke2_next_move = self.poke1.start_status["Delayed"]
            poke2_move = "Delayed"
            del self.poke1.start_status["Delayed"]

        if "Flinch" in self.poke2.start_status.keys():
            if self.poke1.speed < self.poke2.speed:
                poke2_move = "Flinched"
