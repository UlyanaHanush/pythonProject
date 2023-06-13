import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
'''
1.Plot Total Sales Per Month for Year 2011.  How the total sales haveincreased over months in Year 2011. Which month has lowest Sales?
'''
df = pd.read_csv('C:/Users/Uli/Downloads/777_m5_datasets_v1.0/BigMartSalesData.csv', delimiter=',')
print(df.columns)
year2011 = df[df['Year'] == 2011]
grouph = year2011[['Month', 'Amount']].groupby(['Month'], as_index = False).sum()
# print(grouph.min())
# grouph.columns = [''.join(col).rstrip('_') for col in grouph.columns.values]
# grouph.plot(x='Month', y='Amount')
# plt.show()
'''
2.Plot Total Sales Per Month for Year 2011 as Bar Chart.  Is Bar Chart Better to visualize than Simple Plot?
'''
# grouph.plot.bar(x='Month', y='Amount')
# plt.show()
'''
3.Plot Pie Chart for Year 2011 Country Wise. Which Country contributes highest towards sales?
'''
# grouph_country = year2011[['Country', 'Amount']].groupby(['Country'], as_index = False).sum()
# grouph_country.columns = [''.join(col).rstrip('_') for col in grouph_country.columns.values]
# labels=grouph_country['Country']
# grouph_country.plot.pie(y='Amount', figsize=(7,7), shadow=True, labels=None)
# plt.legend(fontsize = 'x-small', framealpha=0, labels=labels)
# plt.show()
'''
4.Plot Scatter Plot for the invoice amounts and see the concentration of amount. 
In which range most of the invoice amounts are concentrated
'''
grouph_InvoiceDate = year2011[['InvoiceDate', 'Amount']].groupby(['InvoiceDate'], as_index = False).mean()
grouph_InvoiceDate.columns = [''.join(col).rstrip('_') for col in grouph_InvoiceDate.columns.values]
plt.scatter(grouph_InvoiceDate['InvoiceDate'], grouph_InvoiceDate['Amount'], marker = 'x',color = 'red', s = 50)
plt.ylim([0, 50])
plt.show()
