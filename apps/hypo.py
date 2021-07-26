import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc


layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(
                dbc.Jumbotron(
                    [
                        html.H1("Hypothesis",
                                className="display-4 text-center font-weight-bold"),
                        html.Hr(className="my-2"),
                        html.H5(
                            "The hypothesis or basic assumption is a temporary answer to a problem that is still a presumption because it still has to be proven true. The alleged answer is a temporary truth,"
                            "which will be tested for truth with data collected through research",
                            className="text-center font-weight-light"
                        ),
                    ]
                ),
                width=12,
            ),
            dbc.Col([

                dcc.Markdown([
                    '''
                    # Two Sample Test

                     It was applied to compare whether the mean difference between the two groups was truly significant or whether it was due to random chance.

                     1. This helps answer questions such as whether member customers have a significant meaning to gross income?

                     2. This helps answer questions such as whether gender customers have a significant meaning to gross income?
                    '''
                ],
                    className="mb-5 mt-5",),
                dcc.Markdown([
                    '''
                    ### Hypothesis 1

                    - The null hypothesis (H0): is that the population mean value for member category customers is less than the population mean value for non-member customers, and the fact that our sample mean for non-member customers is higher than our sample mean for member customers can be described randomly in our sample selection.

                    - The alternative hypothesis (H1): is that the average value of the customer population for the Member category that is closest to the actual goal is greater than the average value for the population of Non-Member customers.

                                                                                            H0: μ1 ≤ μ2
                                                                                            H1: μ1 > μ2
                                                                                            μ1 = Member
                                                                                            μ2 = Normal(Non Member)
                    '''
                ],
                    className="mb-5 mt-5",),
                dcc.Markdown([
                    '''
                    ### Mathematical Proof

                    '''
                ],
                    className="mb-5 mt-5",),
                html.Img(src="/assets/img/membervnonmember.png"),
                dcc.Markdown([
                    '''
                    ### Results
                    α = 0.05
                    - Member sample mean:15.406925702811243 
                    - Member sample std:11.55240693250141
                    - Member Kurtosis:-0.30543442158994694
                    - Non Member sample mean:14.742555780933063
                    - t-statistic:-0.9239383869237462
                    - p-value:0.177872

                    '''
                ],

                    className="mb-5 mt-5",),
                dcc.Markdown([
                    '''
                    ### Conclusion 1
                    
                   This shows that we do not have enough proof to say that Member customers have higher average value than Non Member customers, 
                   so we reject our H1 and accept H0
                    '''
                ], className="mb-5 mt-5",),

                dcc.Markdown([
                    '''
                    ### Hypothesis 2

                    - The null hypothesis (H0) is that the population mean value for female customers is less than the population mean value for male customers, and the fact that our sample mean for male customers is higher than our sample mean for female customers can described randomly in our sample selection.

                    - The alternative hypothesis (H1) is that the average value of the Female category customer population that is closest to the actual goal is greater than the average value of the Male customer population.

                                                                                            H0: μ1 ≤ μ2
                                                                                            H1: μ1 > μ2
                                                                                            μ1 = Female
                                                                                            μ2 = Male

                    '''
                ],
                    className="mb-5 mt-5",),
                dcc.Markdown([
                    '''
                    ### Mathematical Proof

                    '''
                ],
                    className="mb-5 mt-5",),
                html.Img(src="/assets/img/femalevmale.png"),
                dcc.Markdown([
                    '''
                    ### Results
                    α = 0.05
                    - Female sample mean:15.559222222222221
                    - Female sample std:11.376801908092753
                    - Female Kurtosis:-0.36427773073639935
                    - Male sample mean:14.594584677419356
                    - t-statistic:-1.3418813301589028
                    - p-value:0.089971

                    '''
                ],

                    className="mb-5 mt-5",),
                dcc.Markdown([
                    '''
                    ### Conclusion 2
                    
                   This shows that we do not have enough proof to say that female customers have higher average value than male customers, 
                   so we reject our H1 and accept H0
                    '''
                ], className="mb-6 mt-5",),


                dcc.Markdown([
                    '''
                    ## Final Conclusion

                    '''
                ],
                    className="mt-5",),
                html.Img(src="/assets/img/violin.png"),
                dcc.Markdown([
                    '''
                    ##### Members and non-members have a similar distribution when viewed based on the gross income of each customer gender group

                    '''
                ],
                    className="mb-5 mt-3",),

                dcc.Markdown([
                    '''
                    ### Insights

                    - Promotions can be done for groups of members and non-members of each gender because they have the same distribution.
                    - If you want to increase the number of members, there are still many normal customers (non-members) that can be influenced.
                    '''
                ],
                    className="mb-5 mt-5",),
            ],
                className="mb-5 mt-2",
            )
        ])
    ])
])
