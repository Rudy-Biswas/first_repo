import pandas as pd
df = pd.read_excel('First.xlsx')

sorted_column = df.sort_values(['Accounts'], ascending = True)
print(sorted_column)

sorted_column.to_excel('Second.xlsx')

mean = sorted_column['Accounts'].mean()
print(mean)