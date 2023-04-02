from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd

app = Dash(__name__)
server = app.server

app.layout = html.Div([
    # col 1 - left side game interface
    dbc.Col([
        # row a - battle screen
        dbc.Row([], style={'height': '50vh'}),
        # row b - move select
        dbc.Row([
            # move buttons
            html.Button('move 1', id='move-1', n_clicks=0)
        ], style={'height': '50vh'})
    ], style={'width': '60vw', 'height': '100vh'}),

    # col 2 - right side descriptions
    dbc.Col([
        # row a - pokemon describe
        dbc.Row([], style={'height': '50vh'}),
        # row b - move describe
        dbc.Row([], style={'height': '50vh'})
    ], style={'width': '40vw', 'height': '100vh'})
])

if __name__ == "__main__":
    app.run_server(debug=True)