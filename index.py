import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from app import server

from apps import home, hypo, selling

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
            dbc.NavItem(dbc.NavLink('Visualization', href='/apps/visual')),
            dbc.NavItem(dbc.NavLink('Hypothesis', href='/apps/hypo')),
            dbc.NavItem(dbc.NavLink(
                'Dataset', href='https://www.kaggle.com/aungpyaeap/supermarket-sales'))
        ]
    ),
    dcc.Location(id='url'),
    html.Div(id='page-content', children=[])

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
