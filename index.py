from dash import html, dcc, State
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from app import app
from pages import poke_choose, battle_page
from components import navbar
from driver import pokemons
from dash.exceptions import PreventUpdate

# Define the navbar
nav = navbar.Navbar()

# Define the index page layout
app.layout = html.Div([
    dcc.Store(id='error', data=False),
    dcc.Location(id='url', refresh=False),
    nav,
    html.Div(id='page-content', children=[]),

    dbc.Modal([
        dbc.ModalHeader(
            dbc.ModalTitle("Invalid Selection")
        ),
        dbc.ModalBody(children='Too many moves selected', id='error-message'),
        dbc.ModalFooter()], id='select-error', is_open=False)
])


# Create the callback to handle mutlipage inputs
@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname')
)
def display_page(pathname):
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
    options = []
    if chosen:
        for move in pokemons[chosen].moveset:
            options.append(move)

    return options

@app.callback(
    [Output('player-pokemon', 'data'),
     Output('player-moves', 'data')],
    [Input('start-game-button', 'n_clicks'),
     Input('pokemon-options', 'value'),
     Input('move-options', 'value')],
    prevent_initial_call=True
)
def pokemon_chosen(started, poke_choice, moves_choice):
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
    if moves_chosen and len(moves_chosen) > 4:
        return True, True
    elif moves_chosen:
        return False, False

    return True, False


# Run the app on localhost:8050
if __name__ == '__main__':
    app.run_server(debug=True)