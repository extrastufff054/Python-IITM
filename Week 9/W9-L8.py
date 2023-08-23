import pandas as pd
scores = pd.read_csv('scores.csv')
print(scores.shape)
print(scores.count())
print(scores['Total'].max())
print(scores['Total'].min())
print(scores['Total'].mean())
print(scores['Total'].sum())
print(scores['Total'].sort_values())
print(scores['Name'], type(scores['Name']))

#---------------------------------------------------------------

print(scores.head()) #prints first 5 rows of the data frame
print(scores.tail()) #print last 5 rows of the data frame

print(scores[scores['Name'] == 'Nisha']) #gives details of the name "Nisha"

# Topper marks based on gender
print(scores[scores['Gender'] == 'M']['Total'].max()) # topper of boys
print(scores[scores['Gender'] == 'F']['Total'].max()) # topper of girls

# Divinding students in 4 different categories
''' based on physics marks 1) >85 - A grade
                           2) 70-85 - B grade
                           3) 60-70 - C grade
                           4) <60 - D grade
Also finding number of students in each category'''

print(scores[scores['Physics']>85].shape[0])
print(scores[scores['Physics'].between(70,85)].shape[0])
print(scores[scores['Physics'].between(60,70)].shape[0])
print(scores[scores['Physics']<60].shape[0])

# --------------------------------------------------------------

subject = ['Mathematics','Physics','Chemistry']
for sub in subject : 
    print('Above 85 in', sub)
    print(scores[(scores['Gender']=='F') & (scores[sub] >85)].shape[0])
    print(scores[(scores['Gender']=='M') & (scores[sub] >85)].shape[0])

# Students above and below average

subject = ['Mathematics','Physics','Chemistry']
for sub in subject :
    print('Students above average and below average in respective gender(Female and Male)')
    avg = scores[sub].mean()
    print(scores[(scores['Gender']=='F') & (scores[sub] >avg)].shape[0])
    print(scores[(scores['Gender']=='M') & (scores[sub] >avg)].shape[0])
    print(scores[(scores['Gender']=='F') & (scores[sub] <avg)].shape[0])
    print(scores[(scores['Gender']=='M') & (scores[sub] <avg)].shape[0])

# Group by feature of pandas

import pandas as pd 
scores = pd.read_csv('scores.csv')
print(scores.groupby('Gender').groups) # Returns all the keys mapped to F and M respectively

# This(groupby()) concept is useful in bining objects 

subject = ['Mathematics','Physics','Chemistry']
for sub in subject : 
    print("Above average students")
    avg = scores[sub].mean()
    print(scores[scores[sub]>avg].groupby('Gender').groups)

