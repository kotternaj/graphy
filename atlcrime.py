import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import csv

df = pd.read_csv('atlcrime.csv', index_col='number', low_memory=False)
pd.set_option('display.max_rows', 500) #set visible rows / columns
df['date'] = pd.to_datetime(df['date'], format='%m/%d/%Y') #convert dates
df['year'] = pd.DatetimeIndex(df['date']).year
plt.style.use('seaborn')
plt.gcf()
plt.gca()
fig, (ax1, ax2, ax3, ax4) = plt.subplots(nrows=4, ncols=1, sharex=True)

year_x = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016]

yrly_rapes = [100, 82, 131, 102, 101, 144, 155, 142]
yrly_homicides = [80, 88, 87, 83, 83, 93, 92, 107]

yrly_robbery_res = [309, 232, 269, 243, 201, 212, 187, 205]
yrly_robbery_com = [282, 207, 215, 179, 284, 221, 235, 201]
# yrly_robbery_ped = [2026, 1659, 1761, 1807, 1865, 1916, 1722, 1501]

yrly_burglary_res = [7406, 6713, 6405, 5262, 4910, 4473, 3923, 3409]
yrly_burglary_nonres = [1678, 1284, 990, 775, 885, 960, 817, 968]
yrly_auto_theft = [5666, 4993, 5248, 5098, 4451, 4125, 4235, 3832]

yrly_larceny_from_veh = [11046, 9213, 8638, 8828, 9286, 9432, 9539, 9980]
yrly_larceny_non_veh = [8439, 8710, 8915, 8558, 8006, 7403, 7099, 6616]
# yrly_agg_assault = [2594, 2589, 2515, 2459, 2231, 2187, 2113, 2170]

ax1.plot(year_x, yrly_rapes, label="Rapes")
ax1.plot(year_x, yrly_homicides, label="Homicides")

ax2.plot(year_x, yrly_robbery_res, label="Robbery (Residence)")
ax2.plot(year_x, yrly_robbery_com, label="Robbery (Commercial)")
# ax3.plot(year_x, yrly_robbery_ped, label="Robbery (Pedestrian)")

ax3.plot(year_x, yrly_burglary_res, label="Burglary (Residence)")
ax3.plot(year_x, yrly_burglary_nonres, label="Burglary (Non-Residence)")
ax3.plot(year_x, yrly_auto_theft, label="Auto Theft")

ax4.plot(year_x, yrly_larceny_from_veh, label="Larceny (from Vehicle)")
ax4.plot(year_x, yrly_larceny_non_veh, label="Larceny (non-Vehicle")

# ax.plot(year_x, yrly_agg_assault, label="Aggravated Assault")

# ax1.set_xlabel('Years')
ax1.set_ylabel('Total')
ax1.set_title('Annual crime rates - Atlanta')
ax1.legend()

# ax2.set_xlabel('Years')
# ax2.set_ylabel('Crimes')
# ax2.set_title('Annual crime rates - Atlanta')
ax2.legend()

# ax3.set_xlabel('Years')
# ax3.set_ylabel('Crimes')
# ax3.set_title('Annual crime rates - Atlanta')
ax3.legend()

ax4.set_xlabel('Years')
# ax4.set_ylabel('Crimes')
# ax3.set_title('Annual crime rates - Atlanta')
ax4.legend()

plt.tight_layout()
plt.grid(True)
# plt.savefig('plot.png')

plt.show()

# def main():
#     y2009 = (df['date'] >= '2009') & (df['date'] < '2010')
#     y2010 = (df['date'] >= '2010') & (df['date'] < '2011')
#     y2011 = (df['date'] >= '2011') & (df['date'] < '2012')
#     y2012 = (df['date'] >= '2012') & (df['date'] < '2013')
#     y2013 = (df['date'] >= '2013') & (df['date'] < '2014')
#     y2014 = (df['date'] >= '2014') & (df['date'] < '2015')
#     y2015 = (df['date'] >= '2015') & (df['date'] < '2016')
#     y2016 = (df['date'] >= '2016') & (df['date'] < '2017')
#
#
#     rape = df['crime'] == 'RAPE'
#     rape2009 = df.loc[rape][y2009]
#     print('Rapes 2009: ', rape2009.count())
#
#     rape2010 = df.loc[rape][y2010]
#     print('Rapes 2010: ', rape2010.count())
#
#     rape2011 = df.loc[rape][y2011]
#     print('Rapes 2011: ', rape2011.count())
#
#     rape2012 = df.loc[rape][y2012]
#     print('Rapes 2012: ', rape2012.count())
#
#     rape2013 = df.loc[rape][y2013]
#     print('Rapes 2009: ', rape2013.count())
#
#     rape2014 = df.loc[rape][y2014]
#     print('Rapes 2014: ', rape2014.count())
#
#     rape2015 = df.loc[rape][y2015]
#     print('Rapes 2015: ', rape2015.count())
#
#     rape2016 = df.loc[rape][y2016]
#     print('Rapes 2016: ', rape2016.count())
#
#
#     homicide = df['crime'] == 'HOMICIDE'
#     homicide2009 = df.loc[homicide][y2009]
#     print('homicides 2009: ', homicide2009.count())
#
#     homicide2010 = df.loc[homicide][y2010]
#     print('homicides 2010: ', homicide2010.count())
#
#     homicide2011 = df.loc[homicide][y2011]
#     print('homicides 2011: ', homicide2011.count())
#
#     homicide2012 = df.loc[homicide][y2012]
#     print('homicides 2012: ', homicide2012.count())
#
#     homicide2013 = df.loc[homicide][y2013]
#     print('homicides 2013: ', homicide2013.count())
#
#     homicide2014 = df.loc[homicide][y2014]
#     print('homicides 2014: ', homicide2014.count())
#
#     homicide2015 = df.loc[homicide][y2015]
#     print('homicides 2015: ', homicide2015.count())
#
#     homicide2016 = df.loc[homicide][y2016]
#     print('homicides 2016: ', homicide2016.count())
#
#
#     burglary_nonres = df['crime'] == 'BURGLARY-NONRES'
#     burglary_nonres2009 = df.loc[burglary_nonres][y2009]
#     print('burglary_nonress 2009: ', burglary_nonres2009.count())
#
#     burglary_nonres2010 = df.loc[burglary_nonres][y2010]
#     print('burglary_nonress 2010: ', burglary_nonres2010.count())
#
#     burglary_nonres2011 = df.loc[burglary_nonres][y2011]
#     print('burglary_nonress 2011: ', burglary_nonres2011.count())
#
#     burglary_nonres2012 = df.loc[burglary_nonres][y2012]
#     print('burglary_nonress 2012: ', burglary_nonres2012.count())
#
#     burglary_nonres2013 = df.loc[burglary_nonres][y2013]
#     print('burglary_nonress 2009: ', burglary_nonres2013.count())
#
#     burglary_nonres2014 = df.loc[burglary_nonres][y2014]
#     print('burglary_nonress 2014: ', burglary_nonres2014.count())
#
#     burglary_nonres2015 = df.loc[burglary_nonres][y2015]
#     print('burglary_nonress 2015: ', burglary_nonres2015.count())
#
#     burglary_nonres2016 = df.loc[burglary_nonres][y2016]
#     print('burglary_nonress 2016: ', burglary_nonres2016.count())
#
#
#     robbery_res = df['crime'] == 'ROBBERY-RESIDENCE'
#     robbery_res2009 = df.loc[robbery_res][y2009]
#     print('robbery_ress 2009: ', robbery_res2009.count())
#
#     robbery_res2010 = df.loc[robbery_res][y2010]
#     print('robbery_ress 2010: ', robbery_res2010.count())
#
#     robbery_res2011 = df.loc[robbery_res][y2011]
#     print('robbery_ress 2011: ', robbery_res2011.count())
#
#     robbery_res2012 = df.loc[robbery_res][y2012]
#     print('robbery_ress 2012: ', robbery_res2012.count())
#
#     robbery_res2013 = df.loc[robbery_res][y2013]
#     print('robbery_ress 2009: ', robbery_res2013.count())
#
#     robbery_res2014 = df.loc[robbery_res][y2014]
#     print('robbery_ress 2014: ', robbery_res2014.count())
#
#     robbery_res2015 = df.loc[robbery_res][y2015]
#     print('robbery_ress 2015: ', robbery_res2015.count())
#
#     robbery_res2016 = df.loc[robbery_res][y2016]
#     print('robbery_ress 2016: ', robbery_res2016.count())
#
#
#     robbery_com = df['crime'] == 'ROBBERY-COMMERCIAL'
#     robbery_com2009 = df.loc[robbery_com][y2009]
#     print('robbery_coms 2009: ', robbery_com2009.count())
#
#     robbery_com2010 = df.loc[robbery_com][y2010]
#     print('robbery_coms 2010: ', robbery_com2010.count())
#
#     robbery_com2011 = df.loc[robbery_com][y2011]
#     print('robbery_coms 2011: ', robbery_com2011.count())
#
#     robbery_com2012 = df.loc[robbery_com][y2012]
#     print('robbery_coms 2012: ', robbery_com2012.count())
#
#     robbery_com2013 = df.loc[robbery_com][y2013]
#     print('robbery_coms 2009: ', robbery_com2013.count())
#
#     robbery_com2014 = df.loc[robbery_com][y2014]
#     print('robbery_coms 2014: ', robbery_com2014.count())
#
#     robbery_com2015 = df.loc[robbery_com][y2015]
#     print('robbery_coms 2015: ', robbery_com2015.count())
#
#     robbery_com2016 = df.loc[robbery_com][y2016]
#     print('robbery_coms 2016: ', robbery_com2016.count())
#
#
#     larceny_from_veh = df['crime'] == 'LARCENY-FROM VEHICLE'
#     larceny_from_veh2009 = df.loc[larceny_from_veh][y2009]
#     print('larceny_from_vehs 2009: ', larceny_from_veh2009.count())
#
#     larceny_from_veh2010 = df.loc[larceny_from_veh][y2010]
#     print('larceny_from_vehs 2010: ', larceny_from_veh2010.count())
#
#     larceny_from_veh2011 = df.loc[larceny_from_veh][y2011]
#     print('larceny_from_vehs 2011: ', larceny_from_veh2011.count())
#
#     larceny_from_veh2012 = df.loc[larceny_from_veh][y2012]
#     print('larceny_from_vehs 2012: ', larceny_from_veh2012.count())
#
#     larceny_from_veh2013 = df.loc[larceny_from_veh][y2013]
#     print('larceny_from_vehs 2009: ', larceny_from_veh2013.count())
#
#     larceny_from_veh2014 = df.loc[larceny_from_veh][y2014]
#     print('larceny_from_vehs 2014: ', larceny_from_veh2014.count())
#
#     larceny_from_veh2015 = df.loc[larceny_from_veh][y2015]
#     print('larceny_from_vehs 2015: ', larceny_from_veh2015.count())
#
#     larceny_from_veh2016 = df.loc[larceny_from_veh][y2016]
#     print('larceny_from_vehs 2016: ', larceny_from_veh2016.count())
#
#
#     auto_theft = df['crime'] == 'AUTO THEFT'
#     auto_theft2009 = df.loc[auto_theft][y2009]
#     print('auto_thefts 2009: ', auto_theft2009.count())
#
#     auto_theft2010 = df.loc[auto_theft][y2010]
#     print('auto_thefts 2010: ', auto_theft2010.count())
#
#     auto_theft2011 = df.loc[auto_theft][y2011]
#     print('auto_thefts 2011: ', auto_theft2011.count())
#
#     auto_theft2012 = df.loc[auto_theft][y2012]
#     print('auto_thefts 2012: ', auto_theft2012.count())
#
#     auto_theft2013 = df.loc[auto_theft][y2013]
#     print('auto_thefts 2009: ', auto_theft2013.count())
#
#     auto_theft2014 = df.loc[auto_theft][y2014]
#     print('auto_thefts 2014: ', auto_theft2014.count())
#
#     auto_theft2015 = df.loc[auto_theft][y2015]
#     print('auto_thefts 2015: ', auto_theft2015.count())
#
#     auto_theft2016 = df.loc[auto_theft][y2016]
#     print('auto_thefts 2016: ', auto_theft2016.count())
#
#
#     larceny_non_veh = df['crime'] == 'LARCENY-NON VEHICLE'
#     larceny_non_veh2009 = df.loc[larceny_non_veh][y2009]
#     print('larceny_non_vehs 2009: ', larceny_non_veh2009.count())
#
#     larceny_non_veh2010 = df.loc[larceny_non_veh][y2010]
#     print('larceny_non_vehs 2010: ', larceny_non_veh2010.count())
#
#     larceny_non_veh2011 = df.loc[larceny_non_veh][y2011]
#     print('larceny_non_vehs 2011: ', larceny_non_veh2011.count())
#
#     larceny_non_veh2012 = df.loc[larceny_non_veh][y2012]
#     print('larceny_non_vehs 2012: ', larceny_non_veh2012.count())
#
#     larceny_non_veh2013 = df.loc[larceny_non_veh][y2013]
#     print('larceny_non_vehs 2009: ', larceny_non_veh2013.count())
#
#     larceny_non_veh2014 = df.loc[larceny_non_veh][y2014]
#     print('larceny_non_vehs 2014: ', larceny_non_veh2014.count())
#
#     larceny_non_veh2015 = df.loc[larceny_non_veh][y2015]
#     print('larceny_non_vehs 2015: ', larceny_non_veh2015.count())
#
#     larceny_non_veh2016 = df.loc[larceny_non_veh][y2016]
#     print('larceny_non_vehs 2016: ', larceny_non_veh2016.count())
#
#
#     robbery_ped = df['crime'] == 'ROBBERY-PEDESTRIAN'
#     robbery_ped2009 = df.loc[robbery_ped][y2009]
#     print('robbery_peds 2009: ', robbery_ped2009.count())
#
#     robbery_ped2010 = df.loc[robbery_ped][y2010]
#     print('robbery_peds 2010: ', robbery_ped2010.count())
#
#     robbery_ped2011 = df.loc[robbery_ped][y2011]
#     print('robbery_peds 2011: ', robbery_ped2011.count())
#
#     robbery_ped2012 = df.loc[robbery_ped][y2012]
#     print('robbery_peds 2012: ', robbery_ped2012.count())
#
#     robbery_ped2013 = df.loc[robbery_ped][y2013]
#     print('robbery_peds 2009: ', robbery_ped2013.count())
#
#     robbery_ped2014 = df.loc[robbery_ped][y2014]
#     print('robbery_peds 2014: ', robbery_ped2014.count())
#
#     robbery_ped2015 = df.loc[robbery_ped][y2015]
#     print('robbery_peds 2015: ', robbery_ped2015.count())
#
#     robbery_ped2016 = df.loc[robbery_ped][y2016]
#     print('robbery_peds 2016: ', robbery_ped2016.count())
#
#
#     burglary_res = df['crime'] == 'BURGLARY-RESIDENCE'
#     burglary_res2009 = df.loc[burglary_res][y2009]
#     print('burglary_ress 2009: ', burglary_res2009.count())
#
#     burglary_res2010 = df.loc[burglary_res][y2010]
#     print('burglary_ress 2010: ', burglary_res2010.count())
#
#     burglary_res2011 = df.loc[burglary_res][y2011]
#     print('burglary_ress 2011: ', burglary_res2011.count())
#
#     burglary_res2012 = df.loc[burglary_res][y2012]
#     print('burglary_ress 2012: ', burglary_res2012.count())
#
#     burglary_res2013 = df.loc[burglary_res][y2013]
#     print('burglary_ress 2009: ', burglary_res2013.count())
#
#     burglary_res2014 = df.loc[burglary_res][y2014]
#     print('burglary_ress 2014: ', burglary_res2014.count())
#
#     burglary_res2015 = df.loc[burglary_res][y2015]
#     print('burglary_ress 2015: ', burglary_res2015.count())
#
#     burglary_res2016 = df.loc[burglary_res][y2016]
#     print('burglary_ress 2016: ', burglary_res2016.count())
#
#
#     agg_assault = df['crime'] == 'AGG ASSAULT'
#     agg_assault2009 = df.loc[agg_assault][y2009]
#     print('agg_assaults 2009: ', agg_assault2009.count())
#
#     agg_assault2010 = df.loc[agg_assault][y2010]
#     print('agg_assaults 2010: ', agg_assault2010.count())
#
#     agg_assault2011 = df.loc[agg_assault][y2011]
#     print('agg_assaults 2011: ', agg_assault2011.count())
#
#     agg_assault2012 = df.loc[agg_assault][y2012]
#     print('agg_assaults 2012: ', agg_assault2012.count())
#
#     agg_assault2013 = df.loc[agg_assault][y2013]
#     print('agg_assaults 2009: ', agg_assault2013.count())
#
#     agg_assault2014 = df.loc[agg_assault][y2014]
#     print('agg_assaults 2014: ', agg_assault2014.count())
#
#     agg_assault2015 = df.loc[agg_assault][y2015]
#     print('agg_assaults 2015: ', agg_assault2015.count())
#
#     agg_assault2016 = df.loc[agg_assault][y2016]
#     print('agg_assaults 2016: ', agg_assault2016.count())
#
#
# if __name__ == "__main__":
#     main()
