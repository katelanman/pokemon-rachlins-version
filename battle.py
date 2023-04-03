#Creating a battle
from Pokemon import Pokemon
class Battle():

    def __init__(self, poke1, poke2):
        self.poke1 = poke1
        self.poke2 = poke2

    def round(self):

        # check start statuses
        if ("burn" in poke1.start_status.keys()):
            poke1.
