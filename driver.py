
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

# for m in moves:
#     if 'SelfDestruct' in moves[m].effects:
#         print(moves[m].name)
#         print(moves[m].effects)

defender = pokemons['Pikachu']
attacker = pokemons['Ivysaur']
move_choice = moves['Explosion']

print(defender.name, defender.health)
print(attacker.name, attacker.health)
move_choice.activate_move(attacker, defender)
print(defender.name, defender.health)
print(attacker.name, attacker.health)

