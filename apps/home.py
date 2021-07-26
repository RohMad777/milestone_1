from dash_bootstrap_components._components.Row import Row
import dash_html_components as html
import dash_bootstrap_components as dbc

# Basic homepage with two cards and two buttons
layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(
                dbc.Jumbotron(
                  [
                      html.H1("Welcome to Dashboard",
                              className="display-4 text-center font-weight-bold"),
                      html.Hr(className="my-2"),
                      html.H5(
                          "The growth of supermarkets in most populated cities are increasing and market competitions are also high. The dataset is one of the historical sales of supermarket company which has recorded in 3 different branches for 3 months data",
                          className="text-center font-weight-bold"
                      ),
                  ]
                  )

            )
        ]),

        dbc.Row([
            dbc.Col(
                dbc.Card(
                    [
                        dbc.CardBody(
                            [
                                html.H4("Visualization",
                                        className="card-title text-center"),
                                html.P(
                                    "Visualization data with, graph, bar, pie, plot",
                                    className="card-text",
                                ),
                                dbc.Button(
                                    "Go Visualization", className="text-center btn-lg", block=True, color="primary", href="/apps/visual"),
                            ]
                        ),
                    ],
                    style={"width": "20rem"},
                ),
                width=6, className="mb-6",
            ),

            dbc.Col(
                dbc.Card(
                    [
                        dbc.CardBody(
                            [
                                html.H4("Hyphotesist",
                                        className="card-title text-center"),
                                html.P(
                                    "Hyphotesist with Two Sample Test",
                                    className="card-text",
                                ),
                                dbc.Button(
                                    "Go Hypothesist", className="text-center btn-lg", block=True, color="primary", href="/apps/hypo"),
                            ]
                        ),
                    ],
                    style={"width": "20rem"},
                ),
                width=6, className="mb-6"
            ),
        ], className="mb-5"),
    ])

])