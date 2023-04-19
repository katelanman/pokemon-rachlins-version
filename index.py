from dash import html, dcc, State
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from app import app
from pages import poke_choose, battle_page
from components import navbar
from move import Move
from pokemon import Pokemon
from battle import Battle
from dash.exceptions import PreventUpdate
from driver import moves, pokemons


battle = {'battle': None}


# Define the navbar
nav = navbar.Navbar()

# Define the index page layout
app.layout = html.Div([
    # placeholder
    html.Div(id='hidden-div', style={'display':'none'}),

    # stored values
    dcc.Store(id='error', data=False),
    dcc.Store(id="player-pokemon", storage_type="session"),
    dcc.Store(id="player-moves", storage_type="session"),
    dcc.Store(id="opponent-pokemon", storage_type="session"),
    dcc.Store(id="battle", storage_type="session"),

    dcc.Location(id='url', refresh=False),
    nav,
    html.Div(id='page-content', children=[]),

    # selection error for game start
    dbc.Modal([
        dbc.ModalHeader(
            dbc.ModalTitle("Invalid Selection")
        ),
        dbc.ModalBody(children='Too many moves selected', id='error-message'),
        dbc.ModalFooter()], id='select-error', is_open=False)
], style={'backgroundColor': '#fcfcfc', 'color': '#414141'})


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname')
)
def display_page(pathname):
    """
    define page layout based on page url
    """
    if pathname == '/':
        return poke_choose.layout
    if pathname == '/battle':
        return battle_page.layout
    else: # if redirected to unknown link
        return "404 Page Error! Please choose a link"


@app.callback(
    Output('move-options', 'options'),
    Input('pokemon-options', 'value'),
    prevent_initial_call=True
)
def get_move_options(chosen):
    """
    display moveset for chosen pokemon
    :param chosen: name of chosen pokemon
    :return: moveset to display
    """
    options = []
    if chosen:
        for move in pokemons[chosen].moveset:
            options.append(moves[move].name)

    return options


@app.callback(
    Output('move-options', 'value'),
    Input('pokemon-options', 'value'),
    prevent_initial_call=True
)
def reset_move_options(chosen):
    """ reset chosen moves on new pokemon select """
    return []


# TODO: add stats
@app.callback(
    Output('select-img', 'src'),
    Input('pokemon-options', 'value'),
    prevent_initial_call=True
)
def select_stats(chosen):
    """ get image and stats for pokemon when clicked on select screen"""
    return pokemons[chosen].picture


@app.callback(
    [Output('player-pokemon', 'data'),
     Output('player-moves', 'data')],
    [Input('start-game-button', 'n_clicks'),
     Input('pokemon-options', 'value'),
     Input('move-options', 'value')],
    prevent_initial_call=True
)
def pokemon_chosen(started, poke_choice, moves_choice):
    """
    store selected pokemon and moveset for game play
    :param started: int; signifies start game button clicked
    :param poke_choice: str; selected pokemon
    :param moves_choice: lst; selected moves
    :return:
    """
    if started:
        return poke_choice, moves_choice

    return None, None


@app.callback(
    Output('opponent-pokemon', 'data'),
    Input('player-pokemon', 'data'),
    prevent_initial_call=True
)
def get_opponent(player):
    if player:
        return pokemons[player].random_opp(pokemons).name

    return None


@app.callback(
    [Output('start-game-button', 'disabled'),
     Output('select-error', 'is_open')],
    Input('move-options', 'value'),
    prevent_initial_call=True
)
def enable_start(moves_chosen):
    """
    enable start button if choices are valid
    :param moves_chosen: lst; moves selected
    :return: - if start game button is disabled
             - if error modal is open
    """
    if moves_chosen and len(moves_chosen) > 4:
        return True, True
    elif moves_chosen:
        return False, False

    return True, False


@app.callback(
    Output('battle', 'data'),
    [Input('player-pokemon', 'data'),
     Input('opponent-pokemon', 'data'),
     Input('start-game-button', 'n_clicks')],
    prevent_initial_call=True
)
def start_battle(player, opp, started):
    if started:
        battle = Battle(pokemons[player], pokemons[opp])
        return {'battle': battle}

    return ''


@app.callback(
    [Output('opponent-name', 'children'),
     Output('player-name', 'children'),
     Output('move-header', 'children')],
    [Input('player-pokemon', 'data'),
     Input('opponent-pokemon', 'data')]
)
def add_names(player_name, opp_name):
    """ places selected pokemon names in interface page """
    return opp_name, player_name, f'What will {player_name} do?'


# TODO: opponent sprite
@app.callback(
    [Output('player-sprite', 'src'),
     Output('opponent-sprite', 'src')],
    [Input('player-pokemon', 'data'),
     Input('opponent-pokemon', 'data')]
)
def get_sprites(player_name, opp_name):
    """ places selected pokemon sprites in interface page """
    return pokemons[player_name].picture, pokemons[opp_name].picture


@app.callback(
    [Output('player-describe', 'children'),
     Output('player-types', 'children'),
     Output('player-hp', 'children'),
     Output('player-status', 'children'),
     Output('player-speed', 'children'),
     Output('player-attack', 'children'),
     Output('player-defense', 'children'),
     Output('player-spattack', 'children'),
     Output('player-spdefense', 'children')],
    Input('player-pokemon', 'data')
)
def player_stat_box(player_name):
    pokemon = pokemons[player_name]
    status = 'None'

    if list(pokemon.start_status.keys()) + list(pokemon.end_status.keys()):
        ls = list(pokemon.start_status.keys()) + list(pokemon.end_status.keys())
        status = ls[0]

    return player_name, pokemon.types, 'hP: ' + str(pokemon.health), 'Status Condition: ' + status, \
           'Speed: ' + str(pokemon.speed), 'Attack: ' + str(pokemon.attack), 'Defense: ' + str(pokemon.defense), \
           'Special Attack: ' + str(pokemon.spattack), 'Special Defense: ' + str(pokemon.spdefense)


@app.callback(
    [Output('opp-describe', 'children'),
     Output('opp-types', 'children'),
     Output('opp-hp', 'children'),
     Output('opp-status', 'children'),
     Output('opp-speed', 'children'),
     Output('opp-attack', 'children'),
     Output('opp-defense', 'children'),
     Output('opp-spattack', 'children'),
     Output('opp-spdefense', 'children')],
    Input('opponent-pokemon', 'data')
)
def player_stat_box(opp_name):
    pokemon = pokemons[opp_name]
    status = 'None'

    if list(pokemon.start_status.keys()) + list(pokemon.end_status.keys()):
        ls = list(pokemon.start_status.keys()) + list(pokemon.end_status.keys())
        status = ls[0]

    return opp_name, pokemon.types, 'hP: ' + str(pokemon.health), 'Status Condition: ' + status, \
           'Speed: ' + str(pokemon.speed), 'Attack: ' + str(pokemon.attack), 'Defense: ' + str(pokemon.defense), \
           'Special Attack: ' + str(pokemon.spattack), 'Special Defense: ' + str(pokemon.spdefense)


@app.callback(
    [Output('move-1', 'children'),
     Output('move-2', 'children'),
     Output('move-3', 'children'),
     Output('move-4', 'children')],
    Input('player-moves', 'data')
)
def get_moves(moves):
    """ places selected pokemon moves in interface page """

    # number of missing moves
    blank = 4 - len(moves)

    moves = moves + ['NO MOVE'] * blank
    return moves


@app.callback(
    [Output('move-2', 'disabled'),
     Output('move-3', 'disabled'),
     Output('move-4', 'disabled')],
    [Input('move-2', 'children'),
     Input('move-3', 'children'),
     Input('move-4', 'children')]
)
def disable_moves(move2, move3, move4):
    """ disable inactive moves (when less than 4 moves have been selected) """
    return [True if move == 'NO MOVE' else False for move in [move2, move3, move4]]


@app.callback(
    Output('error', 'data'),
    [Input('move-1', 'n_clicks_timestamp'),
     Input('move-2', 'n_clicks_timestamp'),
     Input('move-3', 'n_clicks_timestamp'),
     Input('move-4', 'n_clicks_timestamp')],
    [State('player-pokemon', 'data'),
     State('opponent-pokemon', 'data'),
     State('player-moves', 'data'),
     State('battle', 'data')],
    prevent_initial_call=True
)
def play_round(m1, m2, m3, m4, player, opp, moves):
    if m1 or m2 or m3 or m4:
        opp_move = pokemons[opp].choose_random_move()

        # get chosen move
        click_times = [m1, m2, m3, m4]
        move_index = click_times.index(max(click_times))
        move_chosen = moves[move_index]
        print(battle)
        battle.round(move_chosen, opp_move)

    return False


# Run the app on localhost:8050
if __name__ == '__main__':
    app.run_server(debug=True)