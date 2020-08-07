from scipy.interpolate import interp1d
import pandas as pd
import plotly.express as px
import numpy as np

df = pd.read_csv('cov19.csv')
df.rename(columns={"8/4/2020": "cases" }, inplace=True)
list1 = df.cases.values.tolist()
### Interpolating circle radius to given circle range
m = interp1d([1,max(list1)], [5,18])
circle_radius = m(list1)
fig = px.density_mapbox(df, lat='Lat', lon='Long', radius=circle_radius, zoom=0,
                         mapbox_style='open-street-map')
fig.show()
