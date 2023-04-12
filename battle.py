# Creating a battle
from pokemon import Pokemon
from move import Move
import random


class Battle:

    def __init__(self, poke1, poke2):
        self.poke1 = poke1
        self.poke2 = poke2
        blank = Move([-1, 'Blank', 'Normal', 'Status', '999', '0', '100', 'Does nothing', ''])

    def round(self, poke1_move, poke2_move):

        print(f'Pokemon 1 Health: {self.poke1.health}')
        print(f'Pokemon 2 Health: {self.poke2.health}')
        # initialize "next_move" as an empty string
        poke1_next_move = ''
        poke2_next_move = ''

        # check paralysis on both Pokemon since it affects speed and therefore who goes first
        if "Paralyze" in self.poke1.start_status.keys():
            self.poke1.speed = self.poke1.speed // 4

        if "Paralyze" in self.poke2.start_status.keys():
            self.poke2.speed = self.poke2.speed // 4

        # define a faster and slower Pokemon to determine which one goes first
        if self.poke1.speed >= self.poke2.speed:
            faster = self.poke1
            slower = self.poke2
        elif self.poke2.speed > self.poke1.speed:
            faster = self.poke2
            slower = self.poke1

        # check start statuses for the faster Pokemon
        if "Burn" in faster.start_status.keys():
            # burn cuts attack in half
            faster.attack = faster.attack // 2

        if "Paralyze" in faster.start_status.keys():
            # paralysis has a 25% chance of not allowing the Pokemon to move
            if random.random() < .25:
                if self.poke1 == faster:
                    poke1_move = "Paralyzed"
                    poke1_move = Move.blank
                else:
                    poke2_move = "Paralyzed"
                    poke2_move = Move.blank

        if "Sleep" in faster.start_status.keys():
            # sleep can run for 1-4 turns and the Pokemon cannot move during it
            if faster.start_status["Sleep"]["turns"] > 0:
                faster.start_status["Sleep"]["turns"] -= 1
                if faster == self.poke1:
                    poke1_move = "Asleep"
                    poke1_move = Move.blank
                else:
                    poke2_move = "Asleep"
                    poke2_move = Move.blank

        if "Freeze" in faster.start_status.keys():
            # there's a 20% chance of thawing and the Pokemon cannot move while frozen
            if random.random() < .2:
                del faster.start_status["Freeze"]
            else:
                if faster == self.poke1:
                    poke1_move = "Frozen"
                    poke1_move = Move.blank
                else:
                    poke2_move = "Frozen"
                    poke2_move = Move.blank

        if "Confuse" in faster.start_status.keys():
            # Confuse can last 1-4 turns and has a 50% chance of having the user hurt themselves
            if faster.start_status["Confuse"]["turns"] > 0:
                faster.start_status["Confuse"]["turns"] -= 1
            if random.random() < .5:
                if faster == self.poke1:
                    poke1_move = "Confused"
                    poke1_move = Move.blank
                else:
                    poke2_move = "Confused"
                    poke2_move = Move.blank

        if "Delayed" in faster.start_status.keys():
            # these moves will take place next turn, so we keep track of what they are for next turn
            if faster == self.poke1:
                poke1_next_move = self.poke1.start_status["Delayed"]
                poke1_move = "Delayed"
                poke1_move = Move.blank
            else:
                poke2_next_move = self.poke1.start_status["Delayed"]
                poke2_move = "Delayed"
                poke2_move = Move.blank
            del faster.start_status["Delayed"]

        # The faster Pokemon uses its move
        if faster == self.poke1:
            poke1_move.activate_move(faster, slower)
        else:
            poke2_move.activare_move(faster, slower)

        # Check to see if either Pokemon fainted, ending the battle
        if faster.health <= 0:
            return print(slower.name, "Wins!")
        elif slower.health <= 0:
            return print(faster.name, "Wins!")

        # Check the Slower Pokemon's starting Status
        if "Burn" in slower.start_status.keys():
            # burn cuts attack in half
            slower.attack = slower.attack // 2

        if "Paralyze" in slower.start_status.keys():
            # paralysis has a 25% chance of not letting them move
            if random.random() < .25:
                if slower == self.poke2:
                    poke2_move = "Paralyzed"
                    poke2_move = Move.blank
                else:
                    poke1_move = "Paralyzed"
                    poke1_move = Move.blank

        if "Sleep" in slower.start_status.keys():
            # sleep lasts for 1-5 turns and the Pokemon can't move while inflicted
            if slower.start_status["Sleep"]["turns"] > 0:
                slower.start_status["Sleep"]["turns"] -= 1
                if slower == self.poke2:
                    poke2_move == "Asleep"
                    poke2_move = Move.blank
                else:
                    poke1_move == "Asleep"
                    poke1_move = Move.blank

        if "Freeze" in slower.start_status.keys():
            # has a 20% chance of thawing and the Pokemon cannot move while inflicted
            if random.random() < .2:
                del slower.start_status["Freeze"]
            else:
                if slower == self.poke2:
                    poke2_move = "Frozen"
                    poke2_move = Move.blank
                else:
                    poke1_move = "Frozen"
                    poke1_move = Move.blank

        if "Confuse" in slower.start_status.keys():
            # can last 1-4 turns and has a 50% chance of the User hurting themselves
            if slower.start_status["Confuse"]["turns"] > 0:
                slower.start_status["Confuse"]["turns"] -= 1
            if random.random() < .5:
                if slower == self.poke2:
                    poke2_move = "Confused"
                    poke2_move = Move.blank
                else:
                    poke1_move = "Confused"
                    poke1_move = Move.blank

        if "Delayed" in slower.start_status.keys():
            # these moves will take place next turn, so we keep track of what they are for next turn
            if slower == self.poke2:
                poke2_next_move = self.poke2.start_status["Delayed"]
                poke2_move = "Delayed"
                poke2_move = Move.blank
            else:
                poke1_next_move = self.poke1.start_status["Delayed"]
                poke1_move = "Delayed"
                poke1_move = Move.blank
            del slower.start_status["Delayed"]


        if "Flinch" in slower.start_status.keys():
            # if a Pokemon has the Flinch status they cannot move that turn
            if slower == self.poke2:
                poke2_move = "Flinched"
                poke2_move = Move.blank
            else:
                poke1_move = "Flinched"
                poke1_move = Move.blank
            del slower.start_status["Flinched"]

        # Have the slower Pokemon use its move
        if slower == self.poke1:
            poke1_move.activate_move(slower, faster)
        else:
            poke2_move.activate_move(slower, faster)

        # Check to see if either Pokemon Fainted, ending the battle
        if faster.health <= 0:
            return print(slower.name, "Wins!")
        elif slower.health <= 0:
            return print(faster.name, "Wins!")

        # Check end of turn statuses for each Pokemon
        # At the end of the turn poison and burn both take away 1/16th of the
        # effected Pokemon's total hp
        if "Burn" or "Poison" in self.poke1.end_status.keys():
            self.poke1.health -= self.poke1.max_health // 16

        if "Burn" or "Poison" in self.poke2.end_status.keys():
            self.poke2.health -= self.poke2.max_health // 16
        '''
        # Check for badly poisoned which increases damage every turn it's inflicted
        if "Badly Poisoned" in self.poke1.end_status.keys():
            self.poke1.heath -= self.poke1.max_health / \
                                (16 * self.poke1.end_status["Badly Poisoned"]["turns"])
            
        if "Badly Poisoned" in self.poke2.end_status.keys():
            self.poke2.heath -= self.poke2.max_health / \
                                (16 * self.poke2.end_status["Badly Poisoned"]["turns"])
                                
        # Check for Seeded which removes health from victim and adds health to opponent
        if "Seeded" in self.poke1.end_status.keys():
            self.poke1.health -= self.poke1.max_health / 16
            self.poke2.health += self.poke1.max_health / 16
        
        if "Seeded" in self.poke2.end_status.keys():
            self.poke2.health -= self.poke2.max_health / 16
            self.poke1.health += self.poke2.max_health / 16
        '''

        # Check to see if either Pokemon Fainted, ending the battle
        if faster.health <= 0:
            print(slower.name, "Wins!")
            return faster
        elif slower.health <= 0:
            print(faster.name, "Wins!")
            return slower
        
        return self.poke1, self.poke2, poke1_next_move, poke2_next_move





