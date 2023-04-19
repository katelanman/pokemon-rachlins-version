
from move import Move
from pokemon import Pokemon

moves = {} # {name: object}
pokemons = {} # {name: object}

with open('data/moves.csv', 'r', encoding='UTF8') as f:
    f.readline()
    for i in range(165):
        line = f.readline().strip().split(',')
        line_move = Move(line)
        moves[line[1].lower()] = line_move

with open('data/pokemon.csv', 'r', encoding='UTF8') as f:
    f.readline()
    for i in range(151):
        line = f.readline().strip().split(',')
        line_poke = Pokemon(line)
        pokemons[line[1]] = line_poke

# moves['Blank'] = Move([-1, 'Blank', 'Normal', 'Status', '999', '0', '100', 'Does nothing', ''])

# for m in moves:
#     if 'Heal' in moves[m].effects:
#         print(moves[m].name)
#         print(moves[m].effects)

# defender = pokemons['Pikachu']
# attacker = pokemons['Beedrill']
# move_choice = moves['Absorb']
# move_choice2 = moves['Blizzard']
#
# print(defender.name, defender.health)
# print(attacker.name, attacker.health)
# move_choice2.activate_move(defender, attacker)
# move_choice.activate_move(attacker, defender)
# print(defender.name, defender.health)
# print(attacker.name, attacker.health)

# a = pokemons['Mewtwo']
# b = pokemons['Gastly']
# m = moves['DreamEater']
# print(m.activate_move(b, a))


# test_battle = Battle(a, b)
# c = a.get_opponents(pokemons)
# print(c)
# opp = a.random_opp(c, pokemons)
# print("opp name:", opp, "type:", type(opp))
#
# print("opp moves:", a.choose_moves(b, moves))

# test_battle = Battle(a, b)



# c = a.get_opponents(pokemons)
# print(c)
# opp = a.random_opp(c, pokemons)
# print("opp name:", opp, "type:", type(opp))
#
# print("opp moves:", a.choose_moves(b, moves))


# while a.health > 0 and b.health > 0:
#     move_1 = moves[a.pick_move(b, moves)]
#     move_2 = moves[b.pick_move(a, moves)]
#     if type(move_1) == str:
#         move_1 = moves['Blank']
#     if type(move_2) == str:
#         move_2 = moves['Blank']
#     test_battle.round(move_1, move_2)
#
# print(test_battle.log)



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


