import pandas as pd
df=pd.read_csv(r"C:\Users\Dell\Downloads\archive (3)\Social_Network_Ads.csv")
print(df)
df['Gender']=df['Gender'].astype('category')
df['Gender']=df['Gender'].cat.codes
print(df)
df.isnull().sum()
x=df.drop(columns='Age')
y=df['Age']

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=0)
x_train
x_test

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.fit_transform(x_test)
x_train_scaled
x_test_scaled

from sklearn.linear_model import LogisticRegression
log_reg = LogisticRegression(random_state=0).fit(x_train_scaled,y_train)
log_reg.predict(x_train_scaled)
log_reg.score(x_train_scaled,y_train)
log_reg.score(x_test_scaled,y_test)
log_reg1 = LogisticRegression(random_state=0,C = 1,fit_intercept = True).fit(x_train_scaled,y_train)
log_reg1.score(x_train_scaled,y_train)
log_reg1.score(x_test_scaled,y_test)

y_pred = log_reg.predict(x_test)
y_pred

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
cm
