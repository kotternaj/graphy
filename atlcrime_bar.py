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
