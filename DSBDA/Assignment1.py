import pandas as pd

df = pd.read_csv(r"C:\Users\Dell\Downloads\archive\Best Movie by Year Netflix.csv")
print(df)
# df.head(n=5)
# df.tail(n=10)
# df.index
# df.columns
# df.shapes
# df.dtypes
# df.columns.values
# df.describe(include='all')
# df['TITLE']
# df.sort_index(axis=1,ascending=True)
#df.sort_values(by="SCORE")
# df.iloc[5]
# df.iloc[0:3]
#df.loc[:,['TITLE','SCORE']]
# df.loc[:5,:]
# df.iloc[:,:3]
# df.iloc[:2,:3]
# df.isnull().any()
# df.isnull()
#df.isnull().sum()
#df.isnull().sum().sum()
#df.groupby(['TITLE'])['SCORE'].apply(lambda x: x.isnull())
#df['SCORE'].unique()

