import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

df= pd.read_csv(r'C:\Users\Dell\Desktop\Student Information.csv')
display(df)

#isnull
#df.isnull()
# data = pd.isnull(df['Math Score'])
# display(data)

#notnull
#df.notnull()
# data = pd.notnull(df['Math Score'])
# display(data)

#fillna
#df.fillna(1)

#replace
#df.replace(to_replace=np.nan,value=-99)

#dropna
#df.dropna()
#df.dropna(axis = 1)
#df.dropna(axis=0)

#Detecting outlier using Boxplot
# col=['Math Score','Reading Score','Writing Score','Placement Score']
# df.boxplot(col)
# print(np.where(df['Math Score']>90))
# print(np.where(df['Reading Score']<25))
# print(np.where(df['Writing Score']<30))

#Detecting outlier using Scatterplot
# fig, ax=plt.subplots(figsize=(18,10))
# ax.scatter(df['Placement Score'],df['Placement offer count'])
# ax.set_xlabel('Placement Score')
# ax.set_ylabel('Placement offer count')
# ax.set_title('Scatter Plot')
# plt.show()

#Detecting outlier using Z-score
# z=np.abs(stats.zscore(df['Math Score'])) 
# print(z)
# threshold = 0.18
# sample_outliers = np.where(z<threshold)
# print(sample_outliers)

#Histogram
# df['Math Score'].plot(kind='hist')
# df['log_math'] = np.log10(df['Math Score'])
# df['log_math'].plot(kind='hist')