from dash import html, dcc, State
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from app import app
from pages import poke_choose, battle_page
from components import navbar
from driver import pokemons
from move import Move
from dash.exceptions import PreventUpdate

# Define the navbar
nav = navbar.Navbar()

# Define the index page layout
app.layout = html.Div([
    # stored values
    dcc.Store(id='error', data=False),
    dcc.Store(id="player-pokemon", storage_type="session"),
    dcc.Store(id="player-moves", storage_type="session"),

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


# TODO: replace fake with real
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
            options.append(move)

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


# TODO: get opponent name
@app.callback(
    [Output('opponent-name', 'children'),
     Output('player-name', 'children'),
     Output('move-header', 'children'),
     Output('player-describe', 'children'),
     Output('opponent-describe', 'children')],
    Input('player-pokemon', 'data')
)
def add_names(player_name):
    """ places selected pokemon names in interface page """
    return player_name, player_name, f'What will {player_name} do?', \
           player_name, player_name


# TODO: opponent sprite
@app.callback(
    [Output('player-sprite', 'src'),
     Output('opponent-sprite', 'src')],
    Input('player-pokemon', 'data')
)
def get_sprites(player_name):
    """ places selected pokemon sprites in interface page """
    return pokemons[player_name].picture, pokemons[player_name].picture


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


# TODO: tbh i don't know how this is gonna work with the move class and. okay i am decidedly wrong about everyint
# i dont know how the move and battle classes work well enough apparently
@app.callback(
    [Output( ),
     ],
    [Input('move-2', ''),
     Input('player-pokemon', ''),
     Input('opponent-pokemon', '')]
)
def exchange_damage(move2, poke1, poke2):
    # if battle.faster == poke1:
        dif2 = calc_damage(poke1, poke2)
        poke2.health -= dif








# Run the app on localhost:8050
if __name__ == '__main__':
    app.run_server(debug=True)