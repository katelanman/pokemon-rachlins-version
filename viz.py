import plotly.graph_objects as go

# makes heatmap visualization of every pokemon playing against each other
# bruh lmao

from driver import moves, pokemons
from battle import game_round
import copy

def get_heatmap():
    """
    Gives heatmap
    :param:
    :returns:

    """

    pass

def _do_rounds(poke1, poke2, k=100):
    wins = 0
    for i in range(k):
        # print(f'Round {i+1}')
        a = copy.deepcopy(poke1)
        # print(a)
        b = copy.deepcopy(poke2)
        # print(b)
        while a.health > 0 and b.health > 0:
            amove = moves[a.choose_random_move()]
            bmove = moves[b.choose_random_move()]
            game_round(a, b, amove, bmove)
        if a.health > 0:
            wins += 1
    # print(wins)
    return wins


def get_many_battles():
    outer = []
    lst_poke = list(pokemons.keys())
    lst_poke.remove("Ditto")
    for i in lst_poke:
        inner = []
        for j in lst_poke:
            inner.append(_do_rounds(pokemons[i], pokemons[j]))
        outer.append(inner)
        print(f'done with {i}')
    return outer

def main():
    please = get_many_battles()
    print(please)

main()
