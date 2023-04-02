
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

defender = pokemons['Vileplume']
attacker = pokemons['Geodude']
move_choice = moves['Earthquake']

print(move_choice.calc_damage(attacker, defender))



