import pandas as pd
import numpy as py
import matplotlib as mt
from scipy import stats
from sklearn import preprocessing
df = pd.read_csv(r'C:\Users\Dell\Downloads\archive (1)\Speed Dating Data.csv', encoding='latin-1')
#display(df)

#Mean
#df.mean()
#df.loc[:,'round'].mean()
#df.mean(axis=1)[0:4]

#Median
#df.median()
#df.loc[:,'partner'].median()
#df.median(axis=1)[0:5]

#Mode
#df.mode()
#df.loc[:,'pid'].mode

#Minimum
#df.min()
#df.loc[:,'order'].min(skipna=False)

#Maximum
#df.max()
#df.loc[:,'order'].min(skipna=False)

#Standard Derivation
#df.std()
#df.loc[:,'int_corr'].std()

#Group by
df.groupby(['order'])['pid'].mean()
enc = preprocessing.OneHotEncoder()
enc_df = pd.DataFrame(enc.fit_transform(df[['intel_o']]).toarray())
display(enc_df)
df_encode = df.join(enc_df)
display(df_encode)