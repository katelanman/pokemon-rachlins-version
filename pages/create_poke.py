from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
from driver import moves


layout = html.Div([
    html.H1("Create Your Own Pokemon!", style={'margin': '20px'}),
    html.Div([
        html.P("Name:", style={'float': 'left', 'margin': '20px'}),
        dcc.Input(id='create_name', style={'float': 'left', 'marginTop': '20px'})
    ]),
    html.Div([
        html.P("Type:", style={'float': 'left', 'margin': '20px'}),
        dcc.Input(id='create_type', style={'float': 'left', 'marginTop': '20px'})
    ]),
    html.Div([
        html.P("Health:", style={'float': 'left', 'margin': '20px'}),
        dcc.Input(id='create_health', style={'float': 'left', 'marginTop': '20px'})
    ]),
    html.Div([
        html.P("Attack:", style={'float': 'left', 'margin': '20px'}),
        dcc.Input(id='create_attack', style={'float': 'left', 'marginTop': '20px'})
    ]),
    html.Div([
        html.P("Defense:", style={'float': 'left', 'margin': '20px'}),
        dcc.Input(id='create_defense', style={'float': 'left', 'marginTop': '20px'})
    ]),
    html.Div([
        html.P("Special Attack:", style={'float': 'left', 'margin': '20px'}),
        dcc.Input(id='create_spattack', style={'float': 'left', 'marginTop': '20px'})
    ]),
    html.Div([
        html.P("Special Defense:", style={'float': 'left', 'margin': '20px'}),
        dcc.Input(id='create_spdefense', style={'float': 'left', 'marginTop': '20px'})
    ]),
    html.Div([
        html.P("Speed:", style={'float': 'left', 'margin': '20px'}),
        dcc.Input(id='create_speed', style={'float': 'left', 'marginTop': '20px'})
    ]),
    html.Div([
        html.P("Moveset:", style={'float': 'left', 'margin': '20px'}),
        dcc.Checklist(options=moves.keys(), id='create_moves', style={'float': 'left', 'marginTop': '20px'})
    ]),
    html.Div([
        html.P("Image Url:", style={'float': 'left', 'margin': '20px'}),
        dcc.Input(id='create_image', style={'float': 'left', 'marginTop': '20px'})
    ]),
    html.Div([
        html.P("Submit:", style={'float': 'left', 'margin': '20px'}),
        dbc.Button(id='submitted', style={'float': 'left', 'marginTop': '20px'})
    ]),

])