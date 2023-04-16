from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import base64
from pokemon import Pokemon
from driver import pokemons

fake_poke = {'pikachu': 'pikachu', 'snorlax': 'snorlax', 'charizard': 'charizard'}
fake_dict = {'move1': 1, 'move2': 2, 'move3': 3, 'move4': 4}
pokemon = ""
moves = []

# app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

layout = html.Div([
		html.Div([
			html.Div([
				html.H1("Welcome to Pokemon Showdown")
			], style={'width': '100vw', 'height': '10vh', 'borderBottom': '1px solid black'}),
			html.Div([
				html.Div([
					dcc.RadioItems(id='pokemon-options', options=list(pokemons.keys()))
				], id='pokemon-select', style={'width': '45vw', 'height': '75vh', 'backgroundColor': '#E4E4E4',
												'overflow': 'scroll', 'position': 'absolute', 'left': '2.5vw',
												'top': '20vh'}),
				html.Div([
					dbc.Checklist(options=[], id='move-options')
				], id='move-select', style={'width': '45vw', 'height': '75vh', 'backgroundColor': '#E4E4E4',
											'overflow': 'scroll', 'position': 'absolute', 'left': '52.5vw',
											'top': '20vh'})
			])
		])
	])


# # TODO: replace fake with real
# @app.callback(
# 	Output(component_id='move-options', component_property='options'),
# 	Input(component_id='pokemon-options', component_property='value'))
# def get_move_options(chosen):
# 	options = []
# 	print(chosen)
# 	if chosen:
# 		for move in pokemons[chosen].moveset:
# 			options.append(move)
#
# 	return options
#
# @app.callback(
# 	Output("pokemon", "data"),
#	Input("", "")
# )

# @app.callback(
#     [Output('select-error', 'is_open'),
#      Output('new-game-selection', 'is_open', allow_duplicate=True),
#      Output('error-message', 'children')],
#     Input('start-game', 'n_clicks'),
#     State('pokemon-options', 'value'),
#     State('move-options', 'value'),
#     prevent_initial_call=True
# )
# def pokemon_chosen(started, poke_choice, moves_choice):
#     if not poke_choice:
#         return True, True, "Must choose a pokemon"
#
#     if len(poke_choice) != 1:
#         return True, True, "Must select only one pokemon"
#
#     if not moves_choice:
#         return True, True, "Must select moves"
#
#     if len(moves_choice) != 4:
#         return True, True, "Must select exactly 4 moves"
#
#     pokemon = poke_choice
#     moves = moves_choice
#     return False, False, ""
