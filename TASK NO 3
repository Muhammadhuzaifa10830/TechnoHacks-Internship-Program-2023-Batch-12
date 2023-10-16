#PIVOT TABLE


import pandas as pd
df = pd.read_csv('E:\\DATASET\sample_submission.csv')
df.head()

#summarizing data by calculating : Mean, Median ,Max, Min ,Count


import pandas as pd


pivot_table = df.pivot_table(index='Id', values='SalePrice', aggfunc={'SalePrice': ['mean', 'median', 'max', 'min', 'count']})


pivot_table.columns = ['Mean', 'Median', 'Max', 'Min', 'Count',]

print(pivot_table)
