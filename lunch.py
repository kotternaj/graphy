import xlrd
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# app = dash.Dash(__name__)

pd.set_option('display.max_columns', 10)
df = pd.read_excel('lunch.xls')
df.rename(columns = {'Unnamed: 0' : 'year', 'Unnamed: 1' : 'free', 'Unnamed: 2' : 'reduced_price',
                     'Unnamed: 3' : 'full_price', 'Unnamed: 4' : 'total',
                     'Unnamed: 5' : 'total_served', 'Unnamed: 6' : 'pct_free'}, inplace=True)
print(df.head(10))

app.layout = html.Div([
    html.H1("School lunch program", style={'text-align': 'center'}),

    dcc.Dropdown(id='slct_year',
                 options=[{"label": x, "value": x} for x in year],
                 multi=False,
                 value='1969',
                 style={'width': '40%'}
                 ),

    html.Div(id='output_container', children=[]),
    html.Br(),
    dcc.Graph(id='lunch_map', figure={})
])

@app.callback(
    # [Output(component_id='output_container', component_property='children'),
     Output(component_id='lunch_map', component_property='figure'),
    [Input(component_id='slct_year', component_property='value')]
)
def update_graph(option_slctd):
    print(option_slctd)
    container = "The year chosen by user was: {}".format(option_slctd)

    fig = px.line(data_frame=dff, x='Year', y='pct_free', color='pct_free')

    return container, fig


if __name__ == '__main__':
     app.run_server(debug=True)
