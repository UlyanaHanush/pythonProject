import numpy as np
import pandas as pd
import glob
import os
'''
1.Read the three csv files which contains the score of same students in term1 for each Subject
'''
# math = pd.read_csv('for_class\\MathScoreTerm1.csv', delimiter=',')
# dss = pd.read_csv('for_class\\DSScoreTerm1.csv', delimiter=',')
# physics = pd.read_csv('for_class\\PhysicsScoreTerm1.csv', delimiter=',')
'''
2.Remove the name and ethnicity column (to ensure confidentiality)
'''
# math.drop(columns=['Name','Ethinicity'], axis=1, inplace=True)
# dss.drop(columns=['Name','Ethinicity'], axis=1, inplace=True)
# physics.drop(columns=['Name','Ethinicity'], axis=1, inplace=True)
'''
3.Fill missing score data with zero
'''
# math.fillna(0)
# dss.fillna(0)
# physics.fillna(0)
# print(f'{dss.keys()}\n{math.keys()}\n{physics.keys()}')
'''
4.Merge the three files
'''
# os.chdir("for_class")
# extension = 'csv'
# all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
# combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
# combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')
# # combined_csv.drop(columns=['Name','Ethinicity'], axis=1, inplace=True)
# print(combined_csv.keys())
'''
5.Change Sex(M/F) Columnto 1/2 for further analysis
'''
# combined_csv.loc[(combined_csv['Sex']=='M')]=1
# combined_csv.loc[(combined_csv['Sex']=='F')]=2
# print(combined_csv['Sex'])
'''
6.Store the data in new file –ScoreFinal.csv
'''
# ScoreFinal = pd.DataFrame(combined_csv)
# ScoreFinal.to_csv('ScoreFinal.cvs')
'''
1.Convert ethnicity to numericalvalue
'''
# print(combined_csv['Ethinicity'].unique())
# combined_csv.loc[(combined_csv['Ethinicity']=='White American')]=1
# combined_csv.loc[(combined_csv['Ethinicity']=='European American')]=2
# combined_csv.loc[(combined_csv['Ethinicity']=='Hispanic')]=3
# combined_csv.loc[(combined_csv['Ethinicity']=='African American')]=4
# combined_csv.loc[(combined_csv['Ethinicity']=='nan')]=0
# print(combined_csv['Ethinicity'])
'''
2.Fill the missing score for a student to the average of the class
'''
# combined_csv['Score'] = combined_csv['Score'].fillna(combined_csv['Score'].mean())
# print(combined_csv['Score'])
