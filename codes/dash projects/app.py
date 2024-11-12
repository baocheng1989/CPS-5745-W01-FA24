from dash import Dash, html, dash_table
import dash_bootstrap_components as dbc
import pandas as pd

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

df=pd.read_csv('../data/data.csv')

total_student=df.shape[0]
avg_math_score=round(df['MathScore'].mean(),2)
avg_writing_score=round(df['WritingScore'].mean(),2)
avg_reading_score=round(df['ReadingScore'].mean(),2)
avg_total_score = round((df["MathScore"].mean() + df["ReadingScore"].mean() + df["WritingScore"].mean())/3, 2)

# app.layout=[
#     html.H1(children='Student Exam Scores',style={'textAlign':'center'}),
#     html.Hr(),
#     html.div()
#     dash_table.DataTable(data=df.to_dict('records'),page_size=10),
# ]

app.layout=dbc.Container([
    html.H1(children='Student Exam Scores',style={'textAlign':'center','padding':'20px'}),
    html.Hr(),
    # dbc.CardGroup([
    #     dbc.Card(dbc.CardBody([html.H5('Total Student',className='card-title'),html.P(total_student,className='card-text')])),
    #     dbc.Card(dbc.CardBody([html.H5('Avg Math Score',className='card-title'),html.P(avg_math_score,className='card-text')])),
    #     dbc.Card(dbc.CardBody([html.H5('Avg Writing Score',className='card-title'),html.P(avg_writing_score,className='card-text')])),
    #     dbc.Card(dbc.CardBody([html.H5('Avg Reading Score',className='card-title'),html.P(avg_reading_score,className='card-text')])),
    #     # dbc.Card(dbc.CardBody([html.H5('Average Total Score',className='card-title'),html.P(avg_total_score,className='card-text')]))
    # ]),
    dbc.Row([
        dbc.Col(dbc.Card(dbc.CardBody([html.H5('Total Student',className='card-title'),html.P(total_student,className='card-text')]))),
        dbc.Col(dbc.Card(dbc.CardBody([html.H5('Avg Math Score',className='card-title'),html.P(avg_math_score,className='card-text')]))),
        dbc.Col(dbc.Card(dbc.CardBody([html.H5('Avg Writing Score',className='card-title'),html.P(avg_writing_score,className='card-text')]))),
        dbc.Col(dbc.Card(dbc.CardBody([html.H5('Avg Reading Score',className='card-title'),html.P(avg_reading_score,className='card-text')])))
    ],className="mb-4",style={'text-align':'center'}),
    html.Div([
        dbc.Button("Total Score",color='primary',className='total'),
        dbc.Button("Math Score",color='primary',className='math'),
        dbc.Button("Writing Score",color='primary',className='writing'),
        dbc.Button("Reading Score",color='primary',className='reading')
    ], style={'display':'flex','justify-content':'space-between','width':'100%'}),
    # html.Div([
    #     html.H2('Total Student'),
    #     html.P(total_student),
    #     html.H2('Average Math Score'),
    #     html.P(avg_math_score),
    #     html.H2('Average Writing Score'),
    #     html.P(avg_writing_score),
    #     html.H2('Average Reading Score'),
    #     html.P(avg_reading_score),
    #     html.H2('Average Total Score'),
    #     html.P(avg_total_score)
    # ]),
    dash_table.DataTable(data=df.to_dict('records'),page_size=10,style_table={'overflowX':'auto'}), 
    # dbc.Table.from_dataframe(df,bordered=True,striped=True,hover=True,page_size=10)
])

if __name__ == '__main__':
    app.run_server(debug=True)
