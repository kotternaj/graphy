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
        geo_scope='usa',
    )
fig.show()
