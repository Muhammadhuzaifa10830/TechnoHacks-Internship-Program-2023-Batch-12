# Calculate summary statistics (mean, median,mode, standard deviation) for a dataset
# Taking iris datset

import pandas as pd
df = pd.read_csv('E:\DATASET\iris.csv')
df.head()


#Mean median mode and standard davition of SepalLengthCm


df1 = df['SepalLengthCm']
df1
df1.mean()
df1.median()
df1.mode()
df1.std()


#Mean median mode and standard davition of SepalwidththCm

df2 = df['SepalWidthCm']
df2
df2.mean()
df2.median()
df2.mode()
df2.std()


#Mean median mode and standard davition of PetalLengthCm

df3 = df['PetalLengthCm']
df3
df3.mean()
df3.median()
df3.mode()
df3.std()


#Mean median mode and standard davition of PetalWidthCm	

df4 = df['PetalWidthCm']
df4
df4.mean()
df4.median()
df4.mode()
df4.std()

