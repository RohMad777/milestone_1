import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from app import server

from apps import home, selling, hypo

# Create simple navbar with a brand text and 3 links: 2 to internal pages, 1 to original dataset
# This navbar is always displayed on top
app.layout = html.Div([
    dbc.NavbarSimple(
        brand="DASHBOARD",
        brand_href="/apps/home",
        sticky='top',
        color="dark",
        dark=True,
        children=[
            dbc.ButtonGroup(
                [
                    dbc.Button("Visualization",  href='/apps/visual'),
                    dbc.Button("Hypothesis", href='/apps/hypo'),
                    dbc.DropdownMenu(
                        [dbc.DropdownMenuItem('Dataset', href='https://www.kaggle.com/aungpyaeap/supermarket-sales'),
                         dbc.DropdownMenuItem("My Github", href='https://github.com/RohMad777')],
                        label="Data",
                        group=True,
                    ),
                ]
            ),
        ]
    ),

    dcc.Location(id='url'),
    html.Div(id='page-content', children=[]),
    html.Div(
        dbc.Row(dbc.Col(html.Div("© Copyright by RohMad - 2021"), className="text-center"),
                align="center",
                justify="center"
                ),
        className="p-4  bg-dark text-white"
    )

])

# Show page content below the navbar using callback


@app.callback(
    Output(component_id='page-content', component_property='children'),
    [Input(component_id='url', component_property='pathname')])
def display_page(pathname):
    if pathname == '/apps/visual':
        return selling.layout
    elif pathname == '/apps/hypo':
        return hypo.layout
    else:
        return home.layout


if __name__ == '__main__':
    app.run_server(debug=True)
