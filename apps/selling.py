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
df.drop(['invoice_id', 'tax_5%', 'time',
        'cogs', 'gross_margin_perc'], axis=1, inplace=True)
df['date'] = pd.to_datetime(df.date).dt.date
srt = df.sort_values('date', axis=0, ignore_index=True)

layout = html.Div([
    dbc.Container([
        dbc.Row(
            dbc.Col(
                dbc.Jumbotron(
                    [
                        html.H1("Visualization",
                                className="display-4 text-center font-weight-bold"),
                        html.Hr(className="my-2"),
                        html.H5(
                            "Visualization is an engineering in making pictures, diagrams or animations for the appearance of an information",
                            className="text-center font-weight-light"
                        ),
                    ]
                ),
                width=12
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
                        title='Gross Income by Product Line'
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
                        title='Gross Income by City'
                    )
                )
            )
        ]),

        dbc.Row([
            dbc.Col(
                [
                    dcc.Dropdown(
                        id='names',
                        value='payment',
                        options=[{'value': x, 'label': x}
                                 for x in ['payment', 'gender', 'city']],
                        clearable=False
                    ),

                    dcc.Dropdown(
                        id='values',
                        value='gross_inc',
                        options=[{'value': x, 'label': x}
                                 for x in ['gross_inc', 'unit_price']],
                        clearable=False
                    ),
                    dcc.Graph(id="pie-chart"),
                ]
            ),

            dbc.Col(
                [
                    dcc.Checklist(
                        id="checklist",
                        options=[{"label": x, "value": x}
                                 for x in df.product_line.unique()],
                        value=df.product_line[:2],
                        labelStyle={'display': 'inline-block'}
                    ),
                    dcc.Graph(id="line-chart"),
                ]
            ),
        ]),

    ])
])


@app.callback(
    Output("line-chart", "figure"),
    [Input("checklist", "value")])
def update_line_chart(product_line):
    mask = df.product_line.isin(product_line)
    fig = px.line(df[mask],
                  x="date", y="gross_inc", color='gender', ),

    return fig


@app.callback(
    Output("pie-chart", "figure"),
    [Input("names", "value"),
     Input("values", "value")])
def generate_chart(names, values):
    fig = px.pie(df, values=values, names=names, hole=.3)

    return fig


@ app.callback(
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


@ app.callback(
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
