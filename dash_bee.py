import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

df = pd.read_csv("intro_bees.csv")
# print(df)
df = df.groupby(['State', 'ANSI', 'Affected by', 'Year', 'state_code'])[['Pct of Colonies Impacted']].mean()
df.reset_index(inplace=True)
bee_killers = ["Disease", "Other", "Pesticides", "Pests_excl_Varroa", "Unknown", "Varroa_mites"]
print(df[:5])

app.layout = html.Div([
    html.H1("Web Application Dashboards with Dash", style={'text-align': 'center'}),

    dcc.Dropdown(id='slct_impact',
                 options=[{"label": x, "value": x} for x in bee_killers],
                 multi=False,
                 value='Disease',
                 style={'width': '40%'}
                 ),

    html.Div(id='output_container', children=[]),
    html.Br(),
    dcc.Graph(id='my_bee_map', figure={})
])

@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='my_bee_map', component_property='figure')],
    [Input(component_id='slct_impact', component_property='value')]
)
def update_graph(option_slctd):
    print(option_slctd)
    container = "The year chosen by user was: {}".format(option_slctd)

    # dff = df.copy()
    # dff = dff[dff['Year'] == option_slctd]
    # dff = dff[dff['Affected by'] == 'Varroa_mites']

    dff = df.copy()
    dff = dff[dff['Affected by'] == option_slctd]
    dff = dff[(dff['State'] == 'Texas') | (dff['State'] == 'New Mexico') | (dff['State'] == 'New York')]

    # fig = px.line(data_frame=dff, x='Year', y='Pct of Colonies Impacted', color='State')
    fig = px.bar(dff, x='State', y='Pct of Colonies Impacted')
    fig = px.choropleth(
        data_frame=dff,
        locationmode='USA-states',
        locations='state_code',
        scope="usa",
        color='Pct of Colonies Impacted',
        hover_data=['State', 'Pct of Colonies Impacted'],
        color_continuous_scale=px.colors.sequential.YlOrRd,
        labels={'Pct of Colonies Impacted': '% of Bee Colonies'},
        template='plotly_dark'
    )

    return container, fig


if __name__ == '__main__':
     app.run_server(debug=True)
