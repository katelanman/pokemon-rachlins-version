import math
import random
import copy

class Pokemon():
    """
    Pokemon object that represents a Pokemon from Gen 1 to use in fresh battles

    ATTRIBUTES:
        name (str):                 Name of the pokemon
        lv (int):                   Level of Pokemon
        types (lst of str):         Types of the Pokemon (can be 1 or 2)
        health (int):               Level adjusted health (how many hitpoints a Pokemon has before it faints)
        attacker (int):             Level adjusted attack (offensive stat for physical moves)
        defender (int):             Level adjusted defense (defensive stat for physical moves)
        spattack (int):             Level adjusted special attack (offensive stat for special moves)
        spdefense (int):            Level adjusted special defense (offensive stat for special moves)
        speed (int):                Level adjusted speed of Pokemon (stat that determines turn order)
        accuracy (float):           Accuracy of Pokemon (stat for checking if move connects)
        evasion (float):            Evasion of Pokemon (stat for checking if Pokemon dodges an attack)
        moveset (list of str):      List of moves a Pokemon has that ability to use
        actual_moves (list of str): List of moves a Pokemon chooses to use in a battle
        start_status (dict):        Dictionary of current statuses a Pokemon has that activates before their turn
        end_status (dict):          Dictionary of current statuses a Pokemon has that activates after their turn
        picture (str):              Link to picture to be used in battle (currently not implemented)
        max_health (int):           Maximum health a Pokemon has in battle

    METHODS:
        __init__:       Initializes object
        __str__:        Creates string representation of object
        get_stat:       Getter function that returns a stat
        choose_moves:   Chooses actual moves from moveset
    """

    def __init__(self, stats, lv=50):
        """
        Initializes a new Pokemon. Level is defaulted to 50

        :param stats: List of values that represent a row from pokemon.csv, separated by commas
        :param lv (int): Level of Pokemon
        """
        self.name = stats[1]
        self.lv = lv
        self.types = stats[2].split(';')
        self.health = math.floor((int(stats[3]) * 2 * self.lv) / 100 + self.lv + 10)
        self.attack = math.floor((int(stats[4]) * 2 * self.lv) / 100 + 5)
        self.defense = math.floor((int(stats[5]) * 2 * self.lv) / 100 + 5)
        self.spattack = math.floor((int(stats[6]) * 2 * self.lv) / 100 + 5)
        self.spdefense = math.floor((int(stats[7]) * 2 * self.lv) / 100 + 5)
        self.speed = math.floor((int(stats[8]) * 2 * self.lv) / 100 + 5)
        self.accuracy = 1.0
        self.evasion = 1.0
        self.moveset = stats[9].split(';')
        self.actual_moves = self.moveset[:4]
        self.start_status = {}
        self.end_status = {}
        self.picture = stats[-1]
        self.max_health = self.health

    def get_stat(self, stat):
        """
        Simple getter function that gets necessary stat

        :param stat (str): Stat to get
        :return (list): List of stats to get
        """
        if stat == 'attack':
            return [self.attack]
        elif stat == 'defense':
            return [self.defense]
        elif stat == 'special':
            return [self.spattack, self.spdefense]
        elif stat == 'speed':
            return [self.speed]
        elif stat == 'evasion':
            return [self.evasion]
        elif stat == 'accuracy':
            return [self.accuracy]
        else:
            return [self.attack]

    def __str__(self):
        """
        Creates string representation of Pokemon
        :return (str): String representation of Pokemon for printing purposes
        """
        return str(self.name + '\n' + ';'.join(self.types) + '\n' + ';'.join(self.actual_moves))

    def choose_moves(self):
        """
        Chooses 4 moves from available moves to use in battle. Currently chosen randomly, may
        implement more informed choosing soon.
        :return (list): 4 moves to use in battle
        """
        self.actual_moves = random.sample(self.moveset, 4)

    def choose_random_move(self):
        return random.sample(self.actual_moves, 1)[0]

    def pick_move(self, defender, moves):

        dummy = copy.deepcopy(defender)
        move_dmg = {}
        for move in self.actual_moves:
            dummy.wipe()
            move_dmg[move] = moves[move].calc_damage(self, dummy)[0]

        status_moves = []
        for move in move_dmg:
            if move_dmg[move] == 0:
                status_moves.append(move)

        max_dmg = max(move_dmg.values())
        for move in move_dmg:
            if move_dmg[move] == max_dmg:
                strongest = move

        if len(status_moves) >= 1:
            if len(defender.start_status) == 0 and len(defender.end_status) == 0:
                if random.random() <= .5:
                    return random.choice(status_moves)
        return strongest

    def wipe(self):
        self.start_status = {}
        self.end_status = {}
        self.health = self.max_health