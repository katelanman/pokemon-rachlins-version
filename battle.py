# Creating a battle
from pokemon import Pokemon
from move import Move
import random


class Battle:
    paralyzed = Move([-1, '!Paralysis', 'Normal', 'Status', '999', '0', '100', 'is stunned!', {}])
    asleep = Move([-1, '!Asleep', 'Normal', 'Status', '999', '0', '100', 'is sleeping...', {}])
    confused = Move([-1, '!Confuse', 'Normal', 'Physical', '999', '40', '100', 'hurt itself in confusion!', {}])
    blank = Move([-1, '!Blank', 'Normal', 'Status', '999', '0', '100', 'does nothing.', {}])
    frozen = Move([-1, '!Freeze', 'Ice', 'Status', '999', '0', '100', 'is encased in ice...', {}])
    flinched = Move([-1, '!Flinch', 'Normal', 'Status', '999', '0', '100', 'is too scared to move!', {}])

    def __init__(self, poke1, poke2):
        self.poke1 = poke1
        self.poke2 = poke2
        self.faster = poke1
        self.slower = poke2
        self.log = ''
        poke1.wipe()
        poke2.wipe()

    def round(self, poke1_move, poke2_move):

        mdict = {self.poke1: poke1_move, self.poke2: poke2_move}

        self.log += f'{self.poke1.name} Health: {self.poke1.health}\n'
        self.log += f'{self.poke2.name} Health: {self.poke2.health}\n'
        # initialize "next_move" as an empty string
        poke1_next_move = ''
        poke2_next_move = ''

        # check paralysis on both Pokemon since it affects speed and therefore who goes first
        if "Paralyze" in self.poke1.start_status.keys():
            self.poke1.speed = self.poke1.speed // 2

        if "Paralyze" in self.poke2.start_status.keys():
            self.poke2.speed = self.poke2.speed // 2


        # define a faster and slower Pokemon to determine which one goes first
        if self.poke1.speed >= self.poke2.speed:
            self.faster = self.poke1
            self.slower = self.poke2
        else:
            self.faster = self.poke2
            self.slower = self.poke1


        # check start statuses for the faster Pokemon
        if "Burn" in self.faster.start_status.keys():
            # burn cuts attack in half
            self.faster.attack = self.faster.attack // 2

        if "Paralyze" in self.faster.start_status.keys():
            # paralysis has a 25% chance of not allowing the Pokemon to move
            if random.random() < .25:
                mdict[self.faster] = Battle.paralyzed

        if "Sleep" in self.faster.start_status.keys():
            # sleep can run for 1-4 turns and the Pokemon cannot move during it
            if self.faster.start_status["Sleep"]["turns"] > 0:
                self.faster.start_status["Sleep"]["turns"] -= 1
                mdict[self.faster] = Battle.asleep
            else:
                del self.faster.start_status['Sleep']
                self.log += f'{self.faster.name} woke up!\n'

        if "Freeze" in self.faster.start_status.keys():
            # there's a 20% chance of thawing and the Pokemon cannot move while frozen
            if random.random() < .2:
                del self.faster.start_status["Freeze"]
                self.log += f'{self.faster.name} thawed out!'
            else:
                mdict[self.faster] = Battle.frozen

        if "Confuse" in self.faster.start_status.keys():
            # Confuse can last 1-4 turns and has a 50% chance of having the user hurt themselves
            if self.faster.start_status["Confuse"]["turns"] > 0:
                self.faster.start_status["Confuse"]["turns"] -= 1
            if random.random() < .5:
                mdict[self.faster] = Battle.confused

        if "Delayed" in self.faster.start_status.keys():
            # these moves will take place next turn, so we keep track of what they are for next turn
            if self.faster == self.poke1:
                poke1_next_move = self.poke1.start_status["Delayed"]
                poke1_move = Battle.blank
            else:
                poke2_next_move = self.poke1.start_status["Delayed"]
                poke2_move = Battle.blank
            del self.faster.start_status["Delayed"]

        # The faster Pokemon uses its move
        self.log += mdict[self.faster].activate_move(self.faster, self.slower)

        # Check to see if either Pokemon fainted, ending the battle
        if self.faster.health <= 0:
            self.log += str(self.slower.name) + " Wins!\n"
            return self.slower
        elif self.slower.health <= 0:
            self.log += str(self.faster.name) + " Wins!\n"
            return self.faster

        # Check the Slower Pokemon's starting Status
        if "Burn" in self.slower.start_status.keys():
            # burn cuts attack in half
            self.slower.attack = self.slower.attack // 2

        if "Paralyze" in self.slower.start_status.keys():
            # paralysis has a 25% chance of not letting them move
            if random.random() < .25:
                mdict[self.slower] = Battle.paralyzed

        if "Sleep" in self.slower.start_status.keys():
            # sleep lasts for 1-5 turns and the Pokemon can't move while inflicted
            if self.slower.start_status["Sleep"]["turns"] > 0:
                self.slower.start_status["Sleep"]["turns"] -= 1
                mdict[self.slower] = Battle.asleep
            else:
                del self.slower.start_status['Sleep']
                self.log += f'{self.slower.name} woke up!\n'

        if "Freeze" in self.slower.start_status.keys():
            # has a 20% chance of thawing and the Pokemon cannot move while inflicted
            if random.random() < .2:
                del self.slower.start_status["Freeze"]
                self.log += f'{self.slower.name} thawed out!'
            else:
                mdict[self.slower] = Battle.frozen

        if "Confuse" in self.slower.start_status.keys():
            # can last 1-4 turns and has a 50% chance of the User hurting themselves
            if self.slower.start_status["Confuse"]["turns"] > 0:
                self.slower.start_status["Confuse"]["turns"] -= 1
            if random.random() < .5:
                mdict[self.slower] = Battle.confused

        if "Delayed" in self.slower.start_status.keys():
            # these moves will take place next turn, so we keep track of what they are for next turn
            if self.slower == self.poke2:
                poke2_next_move = self.poke2.start_status["Delayed"]
                poke2_move = Battle.blank
            else:
                poke1_next_move = self.poke1.start_status["Delayed"]
                poke1_move = Battle.blank
            del self.lower.start_status["Delayed"]

        if "Flinch" in self.slower.start_status.keys():
            # if a Pokemon has the Flinch status they cannot move that turn
            mdict[self.slower] = Battle.flinched
            del self.slower.start_status["Flinched"]

        # Have the slower Pokemon use its move
        self.log += mdict[self.slower].activate_move(self.slower, self.faster)

        # Check to see if either Pokemon Fainted, ending the battle
        if self.faster.health <= 0:
            self.log += str(self.slower.name) + " Wins!\n"
            return self.slower
        elif self.slower.health <= 0:
            self.log += str(self.faster.name) + " Wins!\n"
            return self.faster

        # Check end of turn statuses for each Pokemon
        # At the end of the turn poison and burn both take away 1/16th of the
        # effected Pokemon's total hp
        if "Burn" in self.poke1.end_status.keys() or "Poison" in self.poke1.end_status.keys():
            dmg = self.poke1.max_health // 16
            self.poke1.health -= dmg
            self.log += f'{self.poke1.name} took {dmg} damage from a status!\n'

        if "Burn" in self.poke2.end_status.keys() or "Poison" in self.poke2.end_status.keys():
            dmg = self.poke1.max_health // 16
            self.poke2.health -= self.poke2.max_health // 16
            self.log += f'{self.poke2.name} took {dmg} damage from a status!\n'
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

        self.log += '---------------\n'
        # Check to see if either Pokemon Fainted, ending the battle
        if self.faster.health <= 0:
            self.log += str(self.slower.name) + " Wins!\n"
            return self.slower
        elif self.slower.health <= 0:
            self.log += str(self.faster.name) + " Wins!\n"
            return self.faster

        return self.poke1, self.poke2, poke1_next_move, poke2_next_move
