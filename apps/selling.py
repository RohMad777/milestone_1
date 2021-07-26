from numpy.core.fromnumeric import product
import plotly.express as px
import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app

df = pd.read_csv('supermarket_sales_clean.csv')
df.drop(['invoice_id', 'unit_price', 'tax_5%', 'total', 'time',
        'cogs', 'gross_margin_perc'], axis=1, inplace=True)
df['date'] = pd.to_datetime(df.date).dt.date
srt = df.sort_values('date', axis=0, ignore_index=True)

layout = html.Div([
    dbc.Container([
        dbc.Row(
            dbc.Col(
                html.H1("Visualization"),
                className="mb-2 mt-2"
            )
        ),


        dbc.Row([
            dbc.Col(
                dcc.Dropdown(
                    id='product-filter',
                    options=[
                        {'label': product_line, 'value': product_line} for product_line in df.product_line.unique()
                    ],
                    value='Health and beauty'
                )
            ),
            dbc.Col(
                dcc.Dropdown(
                    id='payment-filter',
                    options=[
                        {'label': pay, 'value': pay} for pay in df.payment.unique()
                    ],
                    value='Ewallet'
                )
            )
        ]),

        dbc.Row([
            dbc.Col(dcc.Graph(id='graph-1'), width=6),
            dbc.Col(dcc.Graph(id='graph-2'), width=6)
        ]),

        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    id='graph-3',
                    figure=px.scatter(
                        df, x='date', y='gross_inc', color='product_line',
                        title='Total Sales in All Branch by Product Line'
                    )
                )
            ),

            dbc.Col(
                dcc.Graph(
                    id='graph-4',
                    figure=px.bar(
                        srt,
                        x='date',
                        y='gross_inc',
                        color='city',
                        title='Gross Income Over Time'
                    )
                )
            )
        ]),

    ])
])


@app.callback(
    Output('graph-1', 'figure'),
    Input('product-filter', 'value')
)
def update_graph1(product_line):
    filtered = df[df.product_line == product_line]
    fig = px.bar(
        filtered,
        x='city',
        y='gross_inc',
        color='city',
        title=f'Gross income in {product_line}'
    )
    return fig


@app.callback(
    Output('graph-2', 'figure'),
    Input('payment-filter', 'value')
)
def update_graph2(pay):
    filtered = df[df.payment == pay]
    fig = px.violin(
        filtered,
        x='payment',
        y='gross_inc',
        color='customer_type',
        title=f'Payment by {pay}'
    )
    return fig
