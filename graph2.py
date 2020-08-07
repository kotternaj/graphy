from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import csv

width = 0.25
approval = []
disapproval = []

data = pd.read_csv('covid.csv', nrows=4)
appr = data['approve']
dis = data['disapprove']

for item in appr:
    approval.append(item)
for item in dis:
    disapproval.append(item)
print(approval)
party = ('All', 'Repub', 'Dem', 'Independent')
x_indexes = np.arange(len(party))

plt.xlabel('Party Affiliation')
plt.ylabel('Percentage')

plt.bar(x_indexes - width, approval, width=width, label='Approval')
plt.bar(x_indexes, disapproval, color='r', width=width, label='Disapproval')
plt.xticks(x_indexes, party)
plt.legend()
plt.title('Trump approval rating for Covid response (07/21/20)')
plt.tight_layout()
plt.show()

plt.bar(appr, y)
# plt.plot(dis, y)
plt.ylabel('Total responders')
plt.show()


def find_stats(end_date, party):
    data = pd.read_csv('covid.csv')
    ed = data[end_date]
    p = data[party]
    app = data[approve]
    dis = data[disapprove]

    if ed == end_date and p == party:
        return(p, app, dis)

    print(p, app, dis)
# for row in data.rows:
#     if data.[end_date] == '7/21/20' and pollster == 'YouGov':
#
# ]
# for col in data.columns:
#     col_list.append(col)
#
# print(col_list)


#
# pollster = data['pollster']
# # print(pollster)
#
# for row in data range(2,6):
#     print(row)
# total_y = [0,10,20,30,40,50,60,70,80,90,100]
# # approve = int((row['approve']))
# approve = [38]
# x_indexes = np.arange(len(approve))
# plt.bar(x_indexes, total_y, label='Approve')
#
# # disapprove = int((row['disapprove']))
# # print(approve)
# # print(disapprove)
# #
# # plt.bar(disapprove, total_x, label='Disapprove')
#
# plt.xlabel('Approve / Disapprove')
# plt.ylabel('Total')
# plt.legend()

# plt.show()


# if __name__ == '__main__':
#     find_stats('7/21/2020', 'i')
