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
                  ),

            )
        ]),

        dbc.Row([
            dbc.Col(
                dbc.Card(
                    [
                        dbc.CardBody(
                            [
                                dbc.CardImg(
                                    src="/assets/img/visual.png", top=True,),
                                html.H4("Visualization",
                                        className="card-title text-center"),
                                html.P(
                                    "Visualization data with violin, bar, scatter, and pie chart",
                                    className="card-text text-center",
                                ),
                                dbc.Button(
                                    "Go Visualization", className="text-center btn-lg", block=True, color="primary", href="/apps/visual"),
                            ]
                        ),
                    ],
                    style={"width": "80%"},
                ),
                width=4, className="mb-6",
            ),


            dbc.Col(
                dbc.Card(
                    [
                        dbc.CardBody(
                            [
                                dbc.CardImg(
                                    src="/assets/img/hipo.png", top=True,),
                                html.H4("Hypothesis",
                                        className="card-title text-center"),
                                html.P(
                                    "Hypothesis with Two Sample Test",
                                    className="card-text text-center",
                                ),
                                dbc.Button(
                                    "Go Hypothesis", className="text-center btn-lg", block=True, color="primary", href="/apps/hypo"),
                            ]
                        ),
                    ],
                    style={"width": "80%"},
                ),
                width=4, className="mb-6",
            ),
        ],
            justify="around",
            align="end",
            className="mb-5"
        ),
    ], fluid=True)

])
