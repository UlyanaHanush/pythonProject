import numpy as np
import pandas as pd
import setuptools.command.alias
import numpy.random
import matplotlib.pyplot as plt
import seaborn as sns
'''
Extract data from the givenSalaryGender CSV fileand store the data from each column in a separate NumPy array
'''
# arr = pd.read_csv('SalaryGender.csv', delimiter=',')
# Salary = np.array(arr['Salary'])
# Gender = np.array(arr['Gender'])
# Age = np.array(arr['Age'])
# PhD = np.array(arr['PhD'])
'''
2.Find:
1. The number of men with a PhD
2.The number of women with a PhD
'''
# arr = pd.read_csv('SalaryGender.csv', delimiter=',')
# arr = arr.astype(int)
# arrMen = arr[(arr['PhD']==1) & (arr['Gender']==1)]
# print(len(arrMen)-1)
# arrWomen = arr[(arr['PhD']==1) & (arr['Gender']==0)]
# print(len(arrWomen)-1)
'''
3.Store the “Age” and “PhD” columns in one DataFrame
and delete the data of all people who don’t have a PhD from SalaryGender CSV file.
'''
# arr = pd.read_csv('SalaryGender.csv', delimiter=',')
# arrPhD = arr[['Age', 'PhD']].copy()
# arrPhD = arrPhD[arrPhD['PhD']==0]
# arr = arr.drop(np.where(arr['PhD']==0)[0])
# print(arr)
# print(arrPhD)
'''
4.Calculate the total number of people who have a PhD degreefrom SalaryGender CSV file.
'''
# arr = pd.read_csv('SalaryGender.csv', delimiter=',')
# print(len(arr[arr['PhD']==1]))
'''
5.How  do  you  Count  The  Number  Of  Times  Each  Value  Appears  In  An  Array  Of Integers?
[0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9]
Answer should be array([4, 2, 1, 1, 3, 2, 0, 0, 0, 1])
which means 0 comes 4 times, 1 comes 2 times, 2 comes 1 time, 3 comes 1 time and so on.
'''
# arr = pd.read_csv('SalaryGender.csv', delimiter=',')
# for el in arr:
#     count = arr[el].value_counts()
#     print(count.values)
'''
6.Create a numpy array [[0, 1, 2],[ 3, 4, 5],[ 6, 7, 8],[ 9,10, 11]]) and filter the elements greater than 5.
'''
# arr = np.arange(0,12).reshape((4,3))
# filtred = arr[arr>5]
# print(arr)
# print(filtred)
'''
7.Create a numpy array having NaN (Not a Number) and print it.
array([ nan,   1.,   2.,  nan,   3.,   4.,   5.])
Print the same array omitting all elements which are nan
'''
# arr = np.arange(6.)
# arr[0] = np.nan
# newarr = np.insert(arr, 3, np.nan)
# newarr = pd.Series([newarr])
# print(newarr)
# print(newarr[newarr.notnull()])
'''
8.Create  a  10x10  array  with  random  values  and  find  the  minimum  and  maximum values.
'''
# arr = np.random.randint(1,100, (10,10))
# print(f'{arr}\n {arr.min()}\n {arr.max()}')
'''
9.Create a random vector of size 30 and find the mean value.
'''
# arr = np.random.random(30)
# print(arr.mean(),arr)
'''
10.Create numpy array having elements 0 to 10
And negate all the elements between 3 and 9
'''
# arr = np.arange(11)
# arr[4:9] = arr[4:9]*-1
# print(arr)
'''
11.Create a random array of 3 rows and 3 columns and sort it according to 1stcolumn, 2ndcolumn or 3rdcolumn
'''
# cols = 3
# rows = 3
# np.random.seed(0)
# ser = pd.DataFrame(np.random.rand(rows,cols))
# print(ser.sort_values([1]))
'''
12.Create a four dimensions array get sum over the last two axis at once.
'''
# arr1 = np.random.randint(0,15,size=(2,2,2,4))
# print(sum(arr1[1][1][0]), sum(arr1[1][1][1]))
'''
13.Create a random array and swap two rows of an array.
'''
# arr1 = np.arange(9).reshape(3,3)
# print(arr1)
# arr1[:,[0,1]] = arr1[:,[1,0]]
# print(arr1)
'''
14.Create a random matrix and Compute a matrix rank.
'''
# cols = 3
# rows = 3
# np.random.seed(0)
# ser = pd.DataFrame(np.random.rand(rows,cols))
# print(ser)
# print(ser.shape)
'''
15
'''
arr = pd.read_csv('middle_tn_schools.csv', delimiter=',')
# print(arr.keys())
# print(arr.describe())
# arr1 = arr.groupby('reduced_lunch').mean(numeric_only=True)[['school_rating']]
# print(arr1)
# print(arr1.describe())
# print(arr['reduced_lunch'].corr(arr['school_rating']))
# arr.plot('reduced_lunch', 'school_rating', kind = 'scatter', color='green')
# plt.plot(arr['school_rating'], arr['reduced_lunch'], '-', arr['school_rating'], arr['size'], '--')
# plt.show()
