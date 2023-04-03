from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import base64

def fake_type():
    return "Electric?"

app = Dash(__name__)
server = app.server

app.layout = html.Div([
    # col 1 - left side game interface
    html.Div([
        # row a - battle screen
        html.Div([
            # opponent
            html.Div([
                    # stats box
                    html.Div([
                        html.H3('Pokemon Name', style={'position': 'absolute', 'marginTop': '1vh',
                                                       'marginLeft': '1vw'}),

                        # hp box
                        html.Div([
                            html.H4('HP', style={'margin': '3px'}),
                            html.Div([
                                html.Div([], style={'width': '100%', 'height': '100%', 'backgroundColor': 'green'})
                            ], style={'width': '80%', 'height': '60%', 'backgroundColor': 'white',
                                      'position': 'absolute', 'top': '20%', 'left': '18%', 'border': '1px solid black'})

                        ], style={'width': '60%', 'height': '30%', 'marginTop': '5vh', 'marginLeft': '6.7vw',
                                  'backgroundColor': 'darkgrey', 'position': 'relative', 'border': '1.5px solid black'})

                    ], style={'width': '35%', 'height': '35%', 'backgroundColor': '#96c23c', 'float': 'left',
                              'left': '0%', 'top': '20%', 'position': 'absolute'}),

                    # TODO: change images based on user pokemon
                    html.Img(src='https://img.pokemondb.net/sprites/black-white/anim/shiny/snorlax.gif',
                                style={'width': '20%', 'position': 'absolute', 'right': '10%', 'top': '15%',
                                       'float': 'left'})

            ], style={'height': '50%', 'position': 'relative'}),

            # player
            html.Div([
                    html.Div([], style={'width': '30%', 'height': '30%', 'position': 'absolute', 'marginTop': '20%',
                                        'backgroundColor': 'darkgreen'}),

                    html.Img(src='https://img.pokemondb.net/sprites/black-white/anim/normal/pikachu.gif',
                                style={'width': '20%', 'left': '10%', 'top': '25%', 'float': 'left',
                                       'position': 'absolute'}),

                    # stats box
                    html.Div([
                        html.H3('Pokemon Name', style={'position': 'absolute', 'marginTop': '1vh',
                                                       'marginLeft': '1vw'}),

                        # hp box
                        html.Div([
                            html.H4('HP', style={'margin': '3px'}),
                            html.Div([
                                html.Div([], style={'width': '100%', 'height': '100%', 'backgroundColor': 'green'})
                            ], style={'width': '80%', 'height': '60%', 'backgroundColor': 'white',
                                      'position': 'absolute', 'top': '20%', 'left': '18%', 'border': '1px solid black'})

                        ], style={'width': '60%', 'height': '30%', 'marginTop': '5vh', 'marginLeft': '6.7vw',
                                  'backgroundColor': 'darkgrey', 'position': 'relative', 'border': '1.5px solid black'})

                    ], style={'width': '35%', 'height': '35%', 'backgroundColor': '#96c23c', 'float': 'left',
                              'right': '0%', 'top': '30%', 'position': 'absolute'})
            ], style={'height': '50%', 'position': 'relative'})
        ], style={'height': '60vh', 'backgroundColor': 'olivedrab'}),
        # row b - move select
        html.Div([
            # move buttons
            html.Div([
                html.Button('move 1', id='move-1', n_clicks=0,
                            style={'width': '95%', 'height': '13vh', 'marginTop': '1vh',
                                   'backgroundColor': 'pink'}),
                html.Button('move 2', id='move-2', n_clicks=0,
                            style={'width': '95%', 'height': '13vh', 'marginTop': '1vh',
                                   'backgroundColor': 'yellowgreen'})
            ], style={'width': '50%', 'float': 'left'}),
            html.Div([
                html.Button('move 3', id='move-3', n_clicks=0,
                            style={'width': '95%', 'height': '13vh', 'marginTop': '1vh',
                                   'backgroundColor': 'goldenrod'}),
                html.Button('move 4', id='move-4', n_clicks=0,
                            style={'width': '95%', 'height': '13vh', 'marginTop': '1vh',
                                   'backgroundColor': 'lightblue'})
            ], style={'width': '50%', 'float': 'left'})
        ], style={'height': '30vh', 'justifyContent': 'center'})
    ], style={'width': '55vw', 'height': '90vh', 'float': 'left'}),

    # col 2 - right side descriptions
    html.Div([
        # row a - pokemon describe
        html.Div([
            html.H1('Pokemon Description',
                    style={'textIndent': '15px', 'fontWeight': 'bold'})
        ]),
        html.Div([
            html.H4('Name: ' + fake_type(),
                    style={'textIndent': '25px', 'fontWeight': 'bold'}),

            html.H4('Types:',   style={'textIndent': '40px', 'fontWeight': 'bold'}),

            html.H4('hP:', style={'textIndent': '40px', 'fontWeight': 'bold'}),

            html.H4('Stats:',
                     style={'textIndent': '40px', 'fontWeight': 'bold'}),

            html.H4('Status:',
                     style={'textIndent': '40px', 'fontWeight': 'bold'}),

            html.H4('Condition:', style={'textIndent': '40px', 'fontWeight': 'bold'})

        ], style={'height': '45vh', 'float': 'left'}),


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

        # row b - move describe
        html.Div([
            ###
        ], style={'height': '45vh'})

    ], style={'width': '40vw', 'height': '90vh', 'float': 'left'})
])

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

if __name__ == "__main__":
    app.run_server(debug=True)