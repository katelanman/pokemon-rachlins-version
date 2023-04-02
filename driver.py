from move import Move

with open('moves.csv', 'r', encoding='UTF8') as f:
    header = f.readline()
    for i in range(165):
        # print(f'Move {i+1}:')
        test = f.readline().split(',')
        test_move = Move(test[1:])
        if 'SelfDestruct' in test_move.effects:
            print(test_move.desc)
            print(test_move.effects, test_move.pow)
            print('---------------')


