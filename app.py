from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import base64

def fake_type():
    return "Electric?"

def fake_name():
    # make sure names are capitalized
    return "Pikachu?"

fake_poke = {'pikachu': '1', 'snorlax': '2', 'charizard': '3'}
fake_dict = {'move1': 1, 'move2': 2, 'move3': 3, 'move4': 4}
pokemon = ""
moves = []

# app = Dash(__name__)
app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.layout = html.Div([
    dbc.Modal(
        [
            dbc.ModalHeader(
                dbc.ModalTitle("Welcome to Pokemon Showdown"), close_button=False
            ),
            dbc.ModalBody([
                html.Div([
                    dbc.Checklist(options={}, id='pokemon-options')
                ], id='pokemon-select', style={'width': '45vw', 'height': '90%', 'backgroundColor': '#E4E4E4',
                                               'position': 'absolute', 'left': '2.5vw', 'top': '5vh',
                                               'overflow': 'scroll'}),
                html.Div([
                    dbc.Checklist(options={}, id='move-options')
                ], id='move-select', style={'width': '45vw', 'height': '90%', 'backgroundColor': '#E4E4E4',
                                            'position': 'absolute', 'left': '52.5vw', 'top': '5vh',
                                            'overflow': 'scroll'})]
            ),
            dbc.ModalFooter(dbc.Button("Start Game", id="start-game")),
        ],
        id="new-game-selection",
        keyboard=False,
        backdrop="static",
        fullscreen=True,
        is_open=True
    ),

    dbc.Modal([
            dbc.ModalHeader(
                dbc.ModalTitle("Invalid Selection")
            ),
            dbc.ModalBody(children='', id='error-message'),
            dbc.ModalFooter()
    ], id='select-error'),

    # col 1 - left side game interface
    html.Div([
        # row a - battle screen
        html.Div([
            # opponent
            html.Div([
                    # stats box
                    html.Div([
                        # TODO: get pokemon name (prob best to pull as a global variable somehow)
                        html.H3('Pokemon Name', style={'position': 'absolute', 'marginTop': '1vh',
                                                       'marginLeft': '1vw'}),

                        # TODO: function to change HP after damage (should be able to just adjust width of
                        #  green box --> i made it so we can just use the % health as width fingers crossed it works)
                        # hp box
                        html.Div([
                            html.H4('HP', style={'margin': '3px'}),
                            html.Div([
                                html.Div([], style={'width': '100%', 'height': '100%', 'backgroundColor': 'green'})
                            ], style={'width': '80%', 'height': '60%', 'backgroundColor': 'white',
                                      'position': 'absolute', 'top': '20%', 'left': '18%',
                                      'border': '1px solid #919191', 'borderTop': '1px solid #E4E4E4',
                                      'borderLeft': '1px solid #E4E4E4'})

                        ], style={'width': '60%', 'height': '30%', 'marginTop': '5vh', 'marginLeft': '6.7vw',
                                  'backgroundColor': '#C2C2C2', 'position': 'relative',
                                  'border': '1.5px solid #919191', 'borderTop': '1px solid #E4E4E4',
                                  'borderLeft': '1px solid #E4E4E4'})

                    ], style={'width': '35%', 'height': '35%', 'backgroundColor': '#96c23c', 'float': 'left',
                              'left': '0%', 'top': '20%', 'position': 'absolute'}),

                    # TODO: change images based on user pokemon
                    html.Img(src='https://img.pokemondb.net/sprites/black-white/anim/shiny/snorlax.gif',
                                style={'width': '20%', 'position': 'absolute', 'right': '10%', 'top': '15%',
                                       'float': 'left'})

            ], style={'height': '50%', 'position': 'relative'}),

            # player
            html.Div([
                    # TODO: change image
                    html.Img(src='https://img.pokemondb.net/sprites/black-white/anim/normal/pikachu.gif',
                                style={'width': '20%', 'left': '10%', 'top': '25%', 'float': 'left',
                                       'position': 'absolute'}),

                    # stats box
                    html.Div([
                        # TODO: pokemon name
                        html.H3('Pokemon Name', style={'position': 'absolute', 'marginTop': '1vh',
                                                       'marginLeft': '1vw'}),

                        # TODO: implement damage taken fn here
                        # hp box
                        html.Div([
                            html.H4('HP', style={'margin': '3px', 'opacity': '1'}),
                            html.Div([
                                html.Div([], style={'width': '100%', 'height': '100%', 'backgroundColor': 'green'})
                            ], style={'width': '80%', 'height': '60%', 'backgroundColor': 'white',
                                      'position': 'absolute', 'top': '20%', 'left': '18%',
                                      'border': '1px solid #919191', 'borderTop': '1px solid #E4E4E4',
                                      'borderLeft': '1px solid #E4E4E4'})

                        ], style={'width': '60%', 'height': '30%', 'marginTop': '5vh', 'marginLeft': '6.7vw',
                                  'backgroundColor': '#C2C2C2', 'position': 'relative',
                                  'border': '1.5px solid #919191', 'borderTop': '1px solid #E4E4E4',
                                  'borderLeft': '1px solid #E4E4E4'})

                    ], style={'width': '35%', 'height': '35%', 'backgroundColor': '#96c23c', 'float': 'left',
                              'right': '0%', 'top': '30%', 'position': 'absolute'})
            ], style={'height': '50%', 'position': 'relative'})
        ], style={'height': '60vh', 'backgroundColor': 'olivedrab', 'border': '2px solid green',
                  'borderTop': '2px solid yellowgreen', 'borderLeft': '2px solid yellowgreen'}),

        html.Div([
            # TODO: get player pokemon name
            html.P("What will " + " do?", style={'height': '2.5vh', 'margin': '2%', 'fontSize': '20px'}),

            # row b - move select
            html.Div([

                # TODO: get moves
                # move buttons
                html.Div([
                    html.Button('move 1', id='move-1', n_clicks=0,
                                style={'width': '95%', 'height': '13vh', 'marginLeft': '3.5%', 'marginTop': '0',
                                       'backgroundColor': 'pink', 'cursor': 'pointer'}),
                    html.Button('move 2', id='move-2', n_clicks=0,
                                style={'width': '95%', 'height': '13vh', 'marginLeft': '3.5%', 'marginTop': '2.5%',
                                       'backgroundColor': 'yellowgreen', 'cursor': 'pointer'})
                ], style={'width': '50%', 'float': 'left', 'margin': '0 auto'}),
                html.Div([
                    html.Button('move 3', id='move-3', n_clicks=0,
                                style={'width': '95%', 'height': '13vh', 'marginLeft': '1.5%', 'marginTop': '0',
                                       'backgroundColor': 'goldenrod', 'cursor': 'pointer'}),
                    html.Button('move 4', id='move-4', n_clicks=0,
                                style={'width': '95%', 'height': '13vh', 'marginLeft': '1.5%', 'marginTop': '2.5%',
                                       'backgroundColor': 'lightblue', 'cursor': 'pointer'})
                ], style={'width': '50%', 'float': 'left'})
            ], style={'height': '30vh', 'justifyContent': 'center'})
        ], style={'backgroundColor': '#EEEEEE', 'border': '2px solid #E4E4E4', 'borderLeft': '2px solid #C2C2C2',
                  'borderTop': '2px solid #C2C2C2', 'marginTop': '1vh'})
    ], style={'width': '55vw', 'height': '98vh', 'float': 'left'}),

    # col 2 - right side descriptions
    html.Div([
        # player choices
        html.Div([
            html.Button("New Game", id="new-game")
            # pokemon select
            # html.P('choose', style={'float': 'left'}),
            # dcc.Dropdown(['pikachu', 'snorlax', 'jigglypuff', 'charizard'], id='player-pokemon',
            #              style={'width': '8vw', 'float': 'left'}),
            #
            # # moves select
            # html.P('choose', style={'float': 'left'}),
            # dcc.Dropdown(['move1', 'move2', 'move3', 'move4', 'move5'], id='player-moves',
            # #              id="multi-select-error",
            #              multi=True, searchable=True, clearable=True, placeholder="Select Four Moves",
            #              style={'width': '8vw', 'float': 'left'})
        ], style={'width': '95%', 'height': '5%', 'backgroundColor': 'white', 'margin': '0 auto'}),

        # game history
        html.Div([
            # TODO: get game history & style
        ], style={'overflow': 'scroll', 'width': '95%', 'height': '30%', 'backgroundColor': '#FCFCFC',
                  'margin': '2.5%'}),

        # row a - pokemon describe
        html.Div([
            html.H1('Pokemon Description',
                    style={'textIndent': '15px', 'fontWeight': 'bold'})
        ]),

        # TODO: actual pokemon data
        html.Div([
            dbc.Row([
                html.P(f'{fake_name()}', style={'textIndent': '25px', 'fontWeight': 'bold', 'fontSize': '20px',
                                                'float': 'left'}),
                html.P('Types: ' + fake_type(),   style={'textIndent': '40px', 'fontWeight': 'bold',
                                                         'fontSize': '16px'}),
            ], style={'width': '95%', 'height': '20%', 'position': 'absolute'}),

            # TODO: style bc it hates me ??
            dbc.Row([
                html.P('hP:', style={'textIndent': '40px','fontWeight': 'bold'}),
                html.P('Stats:', style={'textIndent': '40px', 'fontWeight': 'bold'}),
                html.P('Status:', style={'textIndent': '40px', 'fontWeight': 'bold'}),
                html.P('Condition:', style={'textIndent': '40px', 'fontWeight': 'bold'})
            ], style={'width': '95%', 'height': '80%', 'textAlign': 'left', 'position': 'absolute', 'top': '20%'})

        ], style={'height': '25%', 'width': '95%', 'backgroundColor': '#FCFCFC',
                  'margin': '2.5%', 'position': 'relative'}),

        # TODO: actual pokemon data
        html.Div([
            dbc.Row([
                html.P('POKEMON', style={'textIndent': '25px', 'fontWeight': 'bold', 'fontSize': '20px',
                                         'float': 'left'}),
                html.P('Types: ' + fake_type(), style={'textIndent': '40px', 'fontWeight': 'bold',
                                                       'fontSize': '16px'}),
            ], style={'width': '95%', 'height': '20%', 'position': 'absolute'}),

            # TODO: style bc it hates me ??
            dbc.Row([
                html.P('hP:', style={'textIndent': '40px', 'fontWeight': 'bold'}),
                html.P('Stats:', style={'textIndent': '40px', 'fontWeight': 'bold'}),
                html.P('Status:', style={'textIndent': '40px', 'fontWeight': 'bold'}),
                html.P('Condition:', style={'textIndent': '40px', 'fontWeight': 'bold'})
            ], style={'width': '95%', 'height': '80%', 'textAlign': 'left', 'position': 'absolute', 'top': '20%'})

        ], style={'height': '25%', 'width': '95%', 'backgroundColor': '#FCFCFC',
                  'margin': '2.5%', 'position': 'relative'}),


        # row a - pokemon describe
        # """
        # html.Div([
        #     html.H4('Pikachu',
        #             style={'textIndent': '25px', 'fontWeight': 'bold'}),
        #
        #     html.P('Electric?idk',   style={'textIndent': '25px', 'fontSize': '16px'}),
        #
        #     html.P('hP val', style={'textIndent': '25px', 'fontSize' : '16px'}),
        #
        #     html.P('3081 idk',
        #              style={'textIndent': '25px', 'fontSize' : '16px'}),
        #
        #     html.P('status',
        #              style={'textIndent': '25px', 'fontSize' : '16px'}),
        #
        #     html.P('shampoo', style={'textIndent': '25px', 'fontSize' : '16px'})
        #
        # ], style={'height': '45vh', 'float': 'left'}),

    # TODO: website font
    ], style={'width': '40vw', 'height': '98vh', 'float': 'left', 'backgroundColor': '#EEEEEE',
              'marginLeft': '1vh', 'border': '2px solid #E4E4E4', 'borderLeft': '2px solid #C2C2C2',
              'borderTop': '2px solid #C2C2C2'})
], style={'backgroundColor': '#FCFCFC', 'color': '#313131'})


'''
@app.callback()
def get_move():
    # somehow get specific moves that player chose
    pass

@app.callback(
    # TODO: determine output
    Input('move-1', 'n-clicks'),
    Input('move-2', 'n-clicks'),
    Input('move-3', 'n-clicks'),
    Input('move-4', 'n-clicks')
)
def execute_move(move1, move2, move3, move4):
    # disable n clicks for all buttons (to enable after move carried out)
    # figure out which move made
    # somehow do damage etc (update status of targeted pokemon)
    pass
    
'''

@app.callback(
    Output("new-game-selection", "is_open"),
    [Input("new-game", "n_clicks")], #Input("start-game", "n_clicks")],
    [State("new-game-selection", "is_open")],
)
def toggle_modal(n_open, is_open):
    if n_open:# or n_close:
        return not is_open
    return is_open

# TODO: replace fake poke with real dict
@app.callback(
    Output('pokemon-options', 'options'),
    Input('pokemon-options', 'options'),
    State('pokemon-options', 'options'))
def get_poke_options(curr, state):
    options = curr
    for key, value in fake_poke.items():
        options[key] = key
    return options

# TODO: replace fake with real
@app.callback(
    Output('move-options', 'options'),
    Input('move-options', 'options'),
    State('move-options', 'options'))
def get_poke_options(curr, state):
    options = curr
    for key, value in fake_dict.items():
        options[key] = key
    return options

@app.callback(
    [Output('select-error', 'is_open'),
     Output('new-game-selection', 'is_open', allow_duplicate=True),
     Output('error-message', 'children')],
    Input('start-game', 'n_clicks'),
    State('pokemon-options', 'value'),
    State('move-options', 'value'),
    prevent_initial_call=True
)
def pokemon_chosen(started, poke_choice, moves_choice):
    if not poke_choice:
        return True, True, "Must choose a pokemon"

    if len(poke_choice) != 1:
        return True, True, "Must select only one pokemon"

    if not moves_choice:
        return True, True, "Must select moves"

    if len(moves_choice) != 4:
        return True, True, "Must select exactly 4 moves"

    pokemon = poke_choice
    moves = moves_choice
    return False, False, ""


if __name__ == "__main__":
    app.run_server(debug=True)