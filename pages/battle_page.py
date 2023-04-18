from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
# from pages.poke_choose import pokemon


layout = html.Div([
    # col 1 - left side game interface
    html.Div([
        # row a - battle screen
        html.Div([
            # opponent
            html.Div([
                    # stats box
                    html.Div([
                        # TODO: get pokemon name
                        html.H3('Pokemon Name', id='opponent-name',
                                style={'position': 'absolute', 'marginTop': '1vh', 'marginLeft': '1vw',
                                       'fontSize': '25px', 'fontFamily': 'impact',
                                       '-webkit-text-stroke-width': '.5px', '-webkit-text-stroke-color': '#e4e4e4'}),

                        # TODO: function to change HP after damage (should be able to just adjust width of
                        #  green box --> i made it so we can just use the % health as width fingers crossed it works)
                        # hp box
                        html.Div([
                            html.H4('HP', style={'margin': '1px 3px', 'fontSize': '2vh'}),
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
                              'left': '0%', 'top': '20%', 'position': 'absolute', 'borderRadius': '0 3px 3px 0'}),

                    # TODO: change images based on user pokemon
                    html.Img(src='https://img.pokemondb.net/sprites/black-white/anim/shiny/snorlax.gif',
                             id='opponent-sprite', style={'width': '20%', 'position': 'absolute', 'right': '10%',
                                                          'top': '15%', 'float': 'left'})

            ], style={'height': '50%', 'position': 'relative'}),

            # player
            html.Div([
                    # TODO: change image
                    html.Img(src='https://img.pokemondb.net/sprites/black-white/anim/normal/pikachu.gif',
                             id='player-sprite', style={'width': '20%', 'left': '10%', 'top': '25%',
                                                        'float': 'left', 'position': 'absolute'}),

                    # stats box
                    html.Div([
                        # TODO: pokemon name
                        html.H3('Pokemon Name', id='player-name',
                                style={'position': 'absolute', 'marginTop': '1vh', 'marginLeft': '1vw',
                                       'fontSize': '25px', 'fontFamily': 'impact',
                                       '-webkit-text-stroke-width': '.5px', '-webkit-text-stroke-color': '#e4e4e4'}),

                        # TODO: implement damage taken fn here
                        # hp box
                        html.Div([
                            html.H4('HP', style={'margin': '1px 3px', 'fontSize': '2vh'}),
                            html.Div([
                                html.Div([], style={'width': '100%', 'height': '100%', 'backgroundColor': 'green',
                                                    'borderRadius': '3px'})
                            ], style={'width': '80%', 'height': '60%', 'backgroundColor': 'white',
                                      'position': 'absolute', 'top': '20%', 'left': '18%',
                                      'border': '1px solid #919191', 'borderTop': '1px solid #E4E4E4',
                                      'borderLeft': '1px solid #E4E4E4', 'borderRadius': '3px'})

                        ], style={'width': '60%', 'height': '30%', 'marginTop': '5vh', 'marginLeft': '6.7vw',
                                  'backgroundColor': '#C2C2C2', 'position': 'relative',
                                  'border': '1.5px solid #919191', 'borderTop': '1px solid #E4E4E4',
                                  'borderLeft': '1px solid #E4E4E4', 'borderRadius': '3px'})

                    ], style={'width': '35%', 'height': '35%', 'backgroundColor': '#96c23c', 'float': 'left',
                              'right': '0%', 'top': '30%', 'position': 'absolute', 'borderRadius': '3px 0 0 3px'})
            ], style={'height': '50%', 'position': 'relative'})
        ], style={'height': '50vh', 'backgroundColor': 'olivedrab', 'border': '2px solid green',
                  'borderTop': '2px solid yellowgreen', 'borderLeft': '2px solid yellowgreen', 'margin': '10px'}),

        html.Div([
            # TODO: get player pokemon name
            html.P("What will your pokemon do?", id="move-header",
                   style={'height': '2.5vh', 'margin': '2%', 'fontSize': '20px'}),

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
                  'borderTop': '2px solid #C2C2C2', 'margin': '10px'})
    ], style={'width': '55vw', 'height': '98vh', 'float': 'left'}),

    # col 2 - right side descriptions
    html.Div([

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
                html.P('POKEMON', id='player-describe',
                       style={'textIndent': '25px', 'fontWeight': 'bold', 'fontSize': '20px',
                                                'float': 'left'}),
                html.P('Types:',   style={'textIndent': '40px', 'fontWeight': 'bold',
                                                         'fontSize': '16px'}),
            ], style={'width': '95%', 'height': '20%', 'position': 'absolute'}),

            dbc.Row([
                html.P('hP:', id='player-hp', style={'textIndent': '40px', 'fontWeight': 'bold'}),
                html.P('Stats:', id='player-stats', style={'textIndent': '40px', 'fontWeight': 'bold'}),
                html.P('Status:', id='player-status', style={'textIndent': '40px', 'fontWeight': 'bold'}),
                html.P('Condition:', id='player-cond', style={'textIndent': '40px', 'fontWeight': 'bold'})
            ], style={'width': '95%', 'height': '80%', 'textAlign': 'left', 'position': 'absolute', 'top': '20%'})

        ], style={'height': '25%', 'width': '95%', 'backgroundColor': '#FCFCFC',
                  'margin': '2.5%', 'position': 'relative'}),

        # TODO: actual pokemon data
        html.Div([
            dbc.Row([
                html.P('POKEMON', id='opponent-describe',
                       style={'textIndent': '25px', 'fontWeight': 'bold', 'fontSize': '20px',
                                         'float': 'left'}),
                html.P('Types:', style={'textIndent': '40px', 'fontWeight': 'bold',
                                                       'fontSize': '16px'}),
            ], style={'width': '95%', 'height': '20%', 'position': 'absolute'}),

            # TODO: style bc it hates me ??
            dbc.Row([
                html.P('hP:', id='opp-hp', style={'textIndent': '40px', 'fontWeight': 'bold'}),
                html.P('Stats:', id='opp-stats', style={'textIndent': '40px', 'fontWeight': 'bold'}),
                html.P('Status:', id='opp-status', style={'textIndent': '40px', 'fontWeight': 'bold'}),
                html.P('Condition:', id='opp-cond', style={'textIndent': '40px', 'fontWeight': 'bold'})
            ], style={'width': '95%', 'height': '80%', 'textAlign': 'left', 'position': 'absolute', 'top': '20%'})

        ], style={'height': '25%', 'width': '95%', 'backgroundColor': '#FCFCFC',
                  'margin': '2.5%', 'position': 'relative'}),

    # TODO: website font
    ], style={'width': '40vw', 'height': '88vh', 'float': 'left', 'backgroundColor': '#EEEEEE',
              'margin': '10px', 'border': '2px solid #E4E4E4', 'borderLeft': '2px solid #C2C2C2',
              'borderTop': '2px solid #C2C2C2'})
], style={'backgroundColor': '#FCFCFC', 'color': '#313131'})
