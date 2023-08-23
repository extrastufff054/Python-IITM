# Why Pandas

'''
Pandas is a Python library that helps you work with data. 
It provides tools to organize, clean, and analyze information in tables, similar to spreadsheets. 
It's like having a supercharged Excel for programming. You can use it to load data from files, manipulate it, and perform calculations easily. 
It's especially useful for working with large datasets and doing data analysis.
'''

# f = open('Scores.csv','r')
# scores = f.readlines()[1:]
# max = 0
# for record in scores :
#     fields = record.split(',')
#     total = int(fields[8])
#     if  total > max :
#         max = total
# print(max)
# f.close()

# Using Pandas

import pandas as pd
scores = pd.read_csv('Scores.csv')
print(scores['Total'].max())

print(scores)
print(scores.head(3))
print(scores.tail(3))
print(scores.shape)
print(scores.count())
print(scores['Total'].max())
print(scores['Total'].min())
print(scores['Total'].mean())
print(scores['Total'].sum())
print(scores['Total'].sort_values())
print(scores['Total'].sort_values(ascending = False))


