import plotly.graph_objects as go
import pandas as pd
import xlrd

df = pd.read_excel('county.xlsx')
df.rename(columns={'Unnamed: 2': 'county_code', 'Unnamed: 1': 'state_code',
                'Unnamed: 6': 'area_name'}, inplace=True)
ga_code = df['state_code'].str.contains('13')
print(ga_code.count())
# ga_county_codes = df[2] == ga_code
# area_name = df[6]
# print(df[us_county_codes, us_counties])
# county_name = df[ga_county, df.loc[6]]
# print(county_name)
# print(ga_county)
