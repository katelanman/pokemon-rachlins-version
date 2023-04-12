from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc

# Define the navbar structure
def Navbar():
    layout = html.Div([
        dbc.NavbarSimple(
            children=[
                dbc.NavItem(dbc.NavLink("New Game", href="/")),
                dbc.NavItem(dbc.NavLink("Start Game", href="/battle")),
            ],
            brand="Pokemon Showdown",
            brand_href="/",
            color="dark",
            dark=True,
        ),
    ])

    return layout
