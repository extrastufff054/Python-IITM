import pandas as pd

data = {'Name' : ['Alice', 'Bob', 'Charlie'], 'Age' : [25,30,28]}

df = pd.DataFrame(data)

print(df)

print('---'*20)
filtered_df = df[df['Age']>26]
df['Gender'] = ['Female','Male','Male']
print(df)
