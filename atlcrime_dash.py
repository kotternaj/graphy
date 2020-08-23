import dash
import dash_core_components as dcc
import dash_html_components as html
# import dash_table_experiments as dt
import pandas as pd
import datetime
# from scrt import MBT

from plotly import graph_objs as go
from plotly.graph_objs import *
from dash.dependencies import Input, Output, State

# Boostrap CSS.
external_stylesheets = ['https://codepen.io/amyoshino/pen/jzXypZ.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.title = 'Atlanta Crime - 2017'

# # API keys and datasets
# mapbox_access_token = MBT
# crime_data = {}

df = pd.read_csv('csv/crime2017.csv')
dfc = df[['occur_date', 'UC2 Literal','x', 'y']]
dfc = dfc.rename(columns={'occur_date': 'date', 'UC2 Literal': 'crime'})
dfc['date'] = pd.to_datetime(dfc['date'])
dfc['month'] = dfc['date'].dt.month
# crimes = dfc.crime.unique().tolist()
# months = dfc.month.unique().tolist()

crime_data = dfc.groupby(['month']).apply(lambda grp: grp.groupby('crime')['month'].agg('count').to_dict()).to_dict()

# for c in crimes:
#     total = dfc['crime'].str.contains(c).sum()
#     crime_data.update({c:total})
print(crime_data)
print(months)
print(dfc.columns)

app.layout = html.Div(
    html.Div([
        html.Div(
            [
                html.Div(
                    [
                        html.P('Choose Crime:'),
                        dcc.Checklist(
                                id = 'crimelist',
                                options=[{"label": x, "value": x} for x in crimes],
                                # style={'width': '40%'},
                                # multi=True,
                                value=['HOMICIDE'],
                                labelStyle={'display': 'inline-block'}
                        ),
                    ],
                    className='six columns',
                    style={'margin-top': '10'}
                ),

            ], className="row"
        ),

        html.Div(
            [
            html.Div([
                    dcc.Graph(
                        id='example-graph'
                    )
                ], className= 'six columns'
                ),

                html.Div([
                    dcc.Graph(
                        id='example-graph-2'
                    )
                ], className= 'six columns'
                )
            ], className="row"
        )
    ], className='ten columns offset-by-one'))

@app.callback(
    dash.dependencies.Output(component_id='example-graph', component_property='figure'),
    [dash.dependencies.Input(component_id='crimelist', component_property='value')])
def update_image_src(selector):
    data = []
    for crime in selector:
        data.append({'x': months, 'y': crimes,
                    'type': 'bar', 'name': crime})
    figure = {
        'data': data,
        'layout': {
            'title': 'Graph 1',
            'xaxis' : dict(
                title='x Axis',
                titlefont=dict(
                family='Courier New, monospace',
                size=20,
                color='#7f7f7f'
            )),
            'yaxis' : dict(
                title='y Axis',
                titlefont=dict(
                family='Helvetica, monospace',
                size=20,
                color='#7f7f7f'
            ))
        }
    }
    return figure

@app.callback(
    dash.dependencies.Output(component_id='example-graph-2', component_property='figure'),
    [dash.dependencies.Input(component_id='crimelist', component_property='value')])
def update_image_src(selector):
    data = []
    for crime in selector:
        data.append({'x': months, 'y': crime_data[crime].value(),
                    'type': 'line', 'name': crime})
    figure = {
        'data': data,
        'layout': {
            'title': 'Graph 2',
            'xaxis' : dict(
                title='x Axis',
                titlefont=dict(
                family='Courier New, monospace',
                size=20,
                color='#7f7f7f'
            )),
            'yaxis' : dict(
                title='y Axis',
                titlefont=dict(
                family='Helvetica, monospace',
                size=20,
                color='#7f7f7f'
            ))
        }
    }
    return figure

if __name__ == '__main__':
    app.run_server(debug=True)
