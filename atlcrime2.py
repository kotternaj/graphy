import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

df = pd.read_csv('atlcrime.csv', low_memory=False)
crimes = ['HOMICIDE', 'RAPE']
df['date'] = pd.to_datetime(df['date'], format='%m/%d/%Y') #convert dates
df['year'] = pd.DatetimeIndex(df['date']).year

df = df.groupby(['crime','year'])[['crime'.count('year')]]
# counts_dict = {}
# for y in df['year']:
#     for c in df['crime']:
#         counts_dict.update(c, c.value_counts())
#         print(counts_dict)
# years = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016]

app.layout = html.Div([
    html.H1("Atlanta Crimes 2009 - 20016", style={'text-align': 'center'}),

    dcc.Dropdown(id='slct_crime',
                 options=[{"label": x, "value": x} for x in crimes],
                 multi=False,
                 value='HOMICIDE',
                 style={'width': '40%'}
                 ),

    html.Div(id='output_container', children=[]),
    html.Br(),
    dcc.Graph(id='my_crime_map', figure={})
])

@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='my_crime_map', component_property='figure')],
    [Input(component_id='slct_crime', component_property='value')]
)

def update_graph(option_slctd):
    print(option_slctd)
    container = "Year chosen: {}".format(option_slctd)

    # rape = df['crime'] == 'RAPE'
    # rape2009 = df.loc[rape][y2009]
    # dff = df.copy()
    # dff = dff[dff['crime'] == option_slctd]
    # dff = dff[(dff['crime'] == 'RAPE') | (dff['crime'] == 'HOMICIDE')]
    #
    fig = px.line(data_frame=df, x='year', y='crime', color='crime')


    return container, fig


if __name__ == '__main__':
     app.run_server(debug=True)
