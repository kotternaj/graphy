import plotly.graph_objects as go
import plotly.figure_factory as ff
import pandas as pd
import xlrd

df = pd.read_csv('statepop.csv')
ga = df[df['STNAME'] == 'Georgia']

values = df['TOT_POP'].tolist()
fips = df['FIPS'].tolist()

fig = ff.create_choropleth(
    fips=fips, values=values, scope=['GA']
)

fig.layout.template = None
fig.show()
# df.rename(columns={'Unnamed: 2': 'county_code', 'Unnamed: 1': 'state_code',
#                 'Unnamed: 6': 'area_name'}, inplace=True)
# ga_county = (df['state_code'] == '13') & (df['area_name'].str.contains('County')) & (df['county_code'] != '000')

# print(df.columns)
# # fips = df['FIPS'].tolist()
#
# ga_counties = df[df['state_code'] == '13']
# remove_rows_0 = ()
#
# fips = ga_counties['fips'].tolist()
# # print(df.loc[ga_county])
# print(fips)
