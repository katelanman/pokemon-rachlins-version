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
        attack (int):               Level adjusted attack (offensive stat for physical moves)
        defense (int):              Level adjusted defense (defensive stat for physical moves)
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
        stat_total (int):           Sum of the stats of a pokemon to get total stats
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
        self.stat_total = self.max_health + self.attack + self.defense + self.spattack + self.spdefense + self.speed

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

    def choose_moves(self, defender, moves):
        """
        Chooses 4 moves from available moves to use in battle. Currently chosen randomly, may
        implement more informed choosing soon.
        :return (list): 4 moves to use in battle
        """
        dummy = copy.deepcopy(defender)

        print("these are the moves:", moves)

        if len(self.moveset) > 4:
            move_dmg = {}
            for move in self.moveset:
                dummy.wipe()
                move_dmg[move] = moves[move].calc_damage(self, dummy)[0]

            status_moves = []
            for move in move_dmg:
                if move_dmg[move] == 0:
                    status_moves.append(move)

            chosen_moves = []

            for i in range(4):
                max_dmg = max(move_dmg.values())
                for move in move_dmg:
                    if move_dmg[move] == max_dmg:
                        strongest = move

                if len(status_moves) >= 1:
                    if len(defender.start_status) == 0 and len(defender.end_status) == 0:
                        if random.random() <= .5:
                            chosen_moves.append(random.choice(status_moves))
                    else:
                        self.moveset.remove(strongest)
                        del move_dmg[strongest]
                        chosen_moves.append(strongest)

            self.actual_moves = chosen_moves

        else:
            chosen_moves = self.actual_moves
            self.actual_moves = chosen_moves

    def choose_random_move(self):
        return random.sample(self.actual_moves, 1)[0]

    def get_opponents(self, pokemons):
        """
        Finds pokemon within a range of +/- 50 points to the total base stats
        :param pokemons (dict): Dictionary of all pokemon names and their corresponding objects
        :return opponents (list): lists of pokemon within 50 points of stats
        """
        opponents = []
        for pokemon in pokemons.keys():
            if abs(self.stat_total - pokemons[pokemon].stat_total) < 50:
                opponents.append(pokemon)
        return opponents

    def random_opp(self, lst_opps, pokemons):
        """
        Gets random opponent for pokemon of similar ability
        :param lst_opps: list of names of possible opponents
        :param pokemons: dict of pokemon objects
        :return: returns random pokemon opponent
        """
        opp = lst_opps[random.randint(0, len(lst_opps) - 1)]
        return pokemons[opp]

    def pick_move(self, defender, moves):

        """
        :param defender:
        :param moves:
        :return: list
        """

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