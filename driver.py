
from move import Move
from pokemon import Pokemon
import math

moves = {} # {name: object}
pokemons = {} # {name: object}

# Moves to not use as implementing them isn't complete (future project ideas)
BLACKLIST = ['Razorwind', 'Whirlwind', 'Fly', 'Bind', 'Wrap', 'Thrash', 'Roar', 'SonicBoom', 'Disable', 'Mist',
             'LowKick', 'Counter', 'SeismicToss', 'LeechSeed', 'PetalDance', 'DragonRage', 'FireSpin', 'Dig',
             'Toxic', 'Rage', 'Teleport', 'NightShade', 'Mimic', 'LightScreen', 'Haze', 'Reflect', 'FocusEnergy',
             'Bide', 'Metronome', 'MirrorMove', 'Clamp', 'DreamEater', 'SkyAttack', 'Transform', 'Psywave',
             'Splash', 'Rest', 'Conversion', 'SuperFang', 'Substitute']
SUSSY = ['Hyperbeam', 'Swift']

# Reads in the move csv and creates Move objects
with open('data/moves.csv', 'r', encoding='UTF8') as f:
    f.readline()
    for i in range(165):
        line = f.readline().strip().split(',')
        if line[0] not in BLACKLIST:
            line_move = Move(line)
            moves[line[1].lower()] = line_move


# Reads in the pokeon csv and creates Pokemon objects
with open('data/pokemon.csv', 'r', encoding='UTF8') as f:
    f.readline()
    for i in range(151):
        stats = f.readline().strip().split(',')

        types = stats[2].split(';')
        name = stats[1]
        health = stats[3]
        attack = stats[4]
        defense = stats[5]
        spattack = stats[6]
        spdefense = stats[7]
        speed = stats[8]
        picture = stats[-2]
        moveset = stats[9].split(';')
        moveset = [x for x in moveset if x not in BLACKLIST]

        line_poke = Pokemon(name, types, health, attack, defense, spattack, spdefense, speed, picture, moveset)

        pokemons[name] = line_poke
    pokemons['Rachlin'] = Pokemon('Rachlin', ['Psychic', 'Grass'], 200, 200, 200, 200, 200, 200,
                                  'https://www.ccs.neu.edu/home/rachlin/python/ds3500/img/john.png',
                                  ['Thunder', 'Flamethrower', 'Blizzard', 'Earthquake'])

# def reset_stats(poke):
#     with open('data/pokemon.csv', 'r', encoding='UTF8') as f:
#         f.readline()
#         for


# a = pokemons['Pikachu']
# b = pokemons['Abra']
# test_battle = Battle(a, b)
#
# while a.health > 0 and b.health > 0:
#     move_1 = moves[a.choose_random_move()]
#     move_2 = moves[b.choose_random_move()]
#     if type(move_1) == str:
#         move_1 = moves['Blank']
#     if type(move_2) == str:
#         move_2 = moves['Blank']
#
#     test_battle.round(move_1, move_2)


