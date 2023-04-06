#Creating a battle
from Pokemon import Pokemon
class Battle():

    def __init__(self, poke1, poke2):
        self.poke1 = poke1
        self.poke2 = poke2

    def round(self, poke1_move, poke2_move):

        # check start statuses
        if "Burn" in self.poke1.start_status.keys():
            self.poke1.attack = self.poke1.attack/2

        if "Paralyze" in self.poke1.start_status.keys():
            self.poke1.speed = self.poke1.speed/4
            random.random





