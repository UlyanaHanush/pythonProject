import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import fitz
import csv
import re
'''
1.You are given a dataset, which is present in the LMS, containing the number of hurricanes occurring
in the United States along the coast of the Atlantic.
Load the data from the dataset into your program and plot a Bar Graph of the data,
takingthe Year as the x-axis and the number of hurricanes occurring as the Y-axis.
'''
# arr = pd.read_csv('Hurricanes.csv', delimiter=',')
# for i in arr:
#     plt.bar(arr['Year'], arr['Hurricanes'])
# plt.show()
'''
2.The dataset given, records data of city temperatures over the years 2014 and 2015.
Plot the histogram of the temperatures over this period for the cities of San Francisco and Moscow.
'''
# arr = pd.read_csv('CityTemps.csv', delimiter=',')
# bins = np.linspace(-50,50,100)
# plt.hist(arr['San Francisco'],bins,alpha=0.5,label='San Francisco')
# plt.hist(arr['Moscow'], bins, alpha=0.5,label='Moscow')
# plt.legend(loc='upper right')
# plt.show()
'''
3.Plot a pie-chart of the number of models released by every manufacturer, recorded in the data provide.
Also mention the name of the manufacture with the largest releases.
'''
# arr = pd.read_csv('Cars2015.csv', delimiter=',')
# grouped = arr.groupby(['Make']).agg({'Model': ['count']})
# grouped = grouped.reset_index()
# grouped_max = grouped['Model']['count'].agg(['idxmax'])
# print(f"the name of the manufacture with the largest releases grouped number {grouped['Make'][grouped_max]}")
#
# plt.pie(grouped['Model']['count'], labels=grouped['Make'])
# plt.show()
'''
4.Create csv file from the data below and read in pandas data frame
Phase 1 -Reading Data
'''
# text = {}
# with fitz.open('c8jj1fnsta.pdf') as doc:
#     for num, page in enumerate(doc.pages()):
#         if num>1:
#             text[num] = page.get_text()
#             text[num] = re.sub(r'Module[\s\S]*Page \d+','',text[num])
#             text[num] = re.sub(r'5. Let[\s\S]*by sex','',text[num])
#             text[num] = text[num].split("\n")
#             del text[num][0]
#             del text[num][-1]
#             for el in range(len(text[num])):
#                 text[num][el] = text[num][el].split(",")
#
# del text[21][-1]
# del text[21][-1]
# del text[21][-1]
# keys = text[2][0]
# del text[2][0]
#
# list = []
# for num in text:
#     for el in text[num]:
#         list.append(el)
# df = pd.DataFrame(list)
# df = df.drop([8], axis=1)
# df.columns=keys
# df.to_csv(r'data.csv', index=False)
'''Phase 2 –Describe the data Describe the data on the unitprice'''
# print(df.describe())
# print(df['unit price'].describe())
'''
Phase 3 –filter the data
Create new dataframe having columns'name','net_price','date' and group all the records according to name
'''
# new_df = df[['name', 'net_price', 'date ']].copy()
# new_df = new_df.astype({'net_price': float})
# grouph = new_df[['name', 'net_price']].groupby(['name'], as_index = False).sum()
# grouph.columns = [''.join(col).rstrip('_') for col in grouph.columns.values]
# grouph.plot(x='name', y='net_price')
# plt.show()
