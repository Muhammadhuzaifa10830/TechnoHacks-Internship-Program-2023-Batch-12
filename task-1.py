# Histogram for iris datasert

import pandas as pd

df = pd.read_csv('E:\DATASET\iris.csv')
df.head()

import matplotlib.pyplot as plt 
import pandas as pd
df = pd.read_csv('E:\DATASET\iris.csv')
sepal_length = df['SepalLengthCm']
plt.hist(sepal_length, bins=15, color='skyblue', edgecolor='black')
plt.xlabel('Sepal Length (cm)') 
plt.ylabel('Frequency')
plt.title('Histogram of Sepal Length in Iris Dataset')
plt.show()



import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('E:\\DATASET\\iris.csv')
sepal_width = df['SepalWidthCm']
plt.hist(sepal_width, bins=15, color='skyblue', edgecolor='black')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')
plt.title('Histogram of Sepal Width in Iris Dataset')
plt.show()


import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('E:\\DATASET\\iris.csv')
petal_length = df['PetalLengthCm']
plt.hist(petal_length, bins=15, color='skyblue', edgecolor='black')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Frequency')
plt.title('Histogram of Petal Length in Iris Dataset')
plt.show()


import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('E:\\DATASET\\iris.csv')
petal_width = df['PetalWidthCm']
plt.hist(petal_width, bins=15, color='skyblue', edgecolor='black')
plt.xlabel('Petal Width (cm)')
plt.ylabel('Frequency')
plt.title('Histogram of Petal Width in Iris Dataset')
plt.show()


