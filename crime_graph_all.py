import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import csv

df = pd.read_csv('atlcrime.csv', index_col='number', low_memory=False)
pd.set_option('display.max_rows', 500) #set visible rows / columns
df['date'] = pd.to_datetime(df['date'], format='%m/%d/%Y') #convert dates
df['year'] = pd.DatetimeIndex(df['date']).year
crimes = df['crime']
years = df['year']

for years, crimes in df.items():
    print(years, crimes)
# crime_list = []
# crime_set = set()
# total_cases = {}
#
# for c in crime:
#     crime_set.add(c)
#
# for c in crime_set:
#     crime_list.append(c)
# print(crime_list)
#
# for c in crime_list:
#     total_cases.update({ c : c.value() })
# print(total_cases)
