import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('bike.csv')
df['coord'] = df['Location 1'].apply(lambda x: x.split('\n')[2])
df['lat'] = df['coord'].apply(lambda x: x.split(',')[0]).str[1:]
df['long'] = df['coord'].apply(lambda x: x.split(',')[1]).str[:-1]

fig = go.Figure(data=go.Scattergeo(
        lon = df['long'],
        lat = df['lat'],
        text = df['Recreation Centers'],
        mode = 'markers',
        # marker_color = df['cnt'],
        ))

fig.update_layout(
        title = 'Most trafficked US airports<br>(Hover for airport names)',
        geo_scope='tx',
    )
fig.show()

import json
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

dfc = pd.read_json('data/tx_county.geojson')
c = dfc.to_json()

df = pd.read_csv('data/bike.csv')

df['coord'] = df['Location 1'].apply(lambda x: x.split('\n')[2])
df['lat'] = df['coord'].apply(lambda x: x.split(',')[0]).str[1:]
df['long'] = df['coord'].apply(lambda x: x.split(',')[1]).str[:-1]

fig1 = px.choropleth_mapbox(df, geojson=c,
                           color_continuous_scale="Viridis",
                           range_color=(0, 12),
                           mapbox_style="carto-positron",
                           zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
                           opacity=0.5,
                           labels={'unemp':'unemployment rate'}
                          )
fig2 = go.Figure(data=go.Scattergeo(
        lon = df['long'],
        lat = df['lat'],
        text = df['Recreation Centers'],
        mode = 'markers'))

fig1.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig2.update_layout(geo_scope='usa')

fig1.show()
fig2.show()
