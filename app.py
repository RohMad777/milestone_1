import dash
import dash_bootstrap_components as dbc

# bootstrap theme: https://bootswatch.com/litera/
external_stylesheets = [dbc.themes.MATERIA]

# Load external stylesheet LITERA from dbc.themes
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Initialize and hold server running
server = app.server
app.config.suppress_callback_exceptions = True
