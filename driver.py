
from move import Move
from pokemon import Pokemon

moves = {}
pokemons = {}

with open('./data/moves.csv', 'r', encoding='UTF8') as f:
    f.readline()
    for i in range(165):
        line = f.readline().split(',')
        line_move = Move(line)
        moves[line[1]] = line_move

with open('./data/pokemon.csv', 'r', encoding='UTF8') as f:
    f.readline()
    for i in range(151):
        line = f.readline().split(',')

        line_poke = Pokemon(line)
        pokemons[line[1]] = line_poke

moves['Blank'] = Move([-1, 'Blank', 'Normal', 'Status', '999', '0', '100', 'Does nothing', ''])

# for m in moves:
#     if 'Heal' in moves[m].effects:
#         print(moves[m].name)
#         print(moves[m].effects)

defender = pokemons['Pikachu']
attacker = pokemons['Beedrill']
move_choice = moves['Absorb']
move_choice2 = moves['Blizzard']

print(defender.name, defender.health)
print(attacker.name, attacker.health)
move_choice2.activate_move(defender, attacker)
move_choice.activate_move(attacker, defender)
print(defender.name, defender.health)
print(attacker.name, attacker.health)

# POISON SLEEP PARALYSIS FROZEN BURN