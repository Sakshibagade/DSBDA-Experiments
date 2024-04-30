import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r"C:\Users\Dell\Downloads\train.csv")
data.head(10)
data.shape
data.columns
data.info()
data.drop(['PassengerId','Cabin'],axis=1, inplace=True)
print("Average Fare: ",round(data['Fare'].mean(),2))
print("Average Age: ",round(data['Age'].mean(),2))

sns.countplot(data['Survived'])
plt.title("Not Survived and Survived")
plt.xlabel("Survived")
plt.ylabel("Count")
plt.show()

first_class_count = (data["Pclass"] == 1).sum()
print("First Class:",first_class_count)
second_class_count = (data["Pclass"] == 2).sum()
print("First Class:",second_class_count)
third_class_count = (data["Pclass"] == 3).sum()
print("First Class:",third_class_count)

labels = ["First class", "Second Class", "Third Class"]
sizes = [first_class_count,second_class_count ,third_class_count]
plt.pie(sizes,labels=labels, autopct= '%1.2f%%')
plt.axis("equal")
plt.title("Class Distribution")
plt.show()

plt.figure(figsize= (16,8))
sns.countplot(x=data["Pclass"],hue=data["Survived"])
plt.title("Survived wrt Class")
plt.xlabel("Classes")
plt.ylabel("Count")
plt.show()

plt.figure(figsize= (16,8))
axs = sns.kdeplot(data.Pclass[data.Survived == 0], label="died")
axs = sns.kdeplot(data.Pclass[data.Survived == 1], label="survived")
plt.title("Survived wrt Class")
plt.xlabel("Classes")
plt.ylabel("Normalized Count")
plt.show()

data.hist(column="Age", bins=80, figsize= (16,8))
plt.title("Age Dist")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

plt.figure(figsize= (16,8))
axs = sns.kdeplot(data.Pclass[data.Survived == 0], shade=True, label="died")
axs = sns.kdeplot(data.Pclass[data.Survived == 1], shade=True, label="survived")
plt.title("Survived wrt Age")
plt.xlabel("Age")
plt.ylabel("Normalized Count")
plt.show()

data.hist(column="Fare", bins=200, figsize= (16,8))
plt.title("Fare Dist")
plt.xlabel("Fare")
plt.ylabel("Count")
plt.show()

survived_above_500 = ((data['Fare']>500) & (data['Survived']==1)).sum()
print("Survived After Paying more than 500 Dollars: ",survived_above_500)
data.loc[data['Fare'] > 500]

plt.figure(figsize=(12,8))
plt.scatter(data['Age'], data['Fare'])
plt.title("Age wrt Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()

male_dead = ((data['Sex']=='male') & (data['Survived']==0)).sum()
print("Men Died: ",male_dead)
male_survived = ((data['Sex']=='male') & (data['Survived']==1)).sum()
print("Men Survived: ",male_survived)

female_dead = ((data['Sex']=='female') & (data['Survived']==0)).sum()
print("Women Died: ",female_dead)
female_survived = ((data['Sex']=='female') & (data['Survived']==1)).sum()
print("Women Survived: ",female_survived)

m_data = (male_dead,male_survived)
f_data = (female_dead,female_survived)
p1 = plt.bar(np.arange(2),(m_data),width=0.4)
p2 = plt.bar(np.arange(2),(f_data),bottom=m_data, width=0.4)
plt.xticks(np.arange(2), ["Men","Women"])
plt.legend((p1[0], p2[0]),("Died","Survived"))
plt.title("Men v/s Women Survival")
plt.show()

sns.countplot(x=data['Embarked'])
plt.title("Boarding station count")
plt.xlabel("Port")
plt.ylabel("Count")
plt.show()

sns.countplot(x=data['Embarked'], hue= data["Survived"])
plt.title("Boarding station count survived")
plt.xlabel("Port")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(12,8))
ax = sns.heatmap(data.corr().abs(), annot=True)
plt.show()

data['Sex'] = data['Sex'].replace('male',1)
data['Sex'] = data['Sex'].replace('female',0)

data['Embarked'] = data['Embarked'].replace('C',1)
data['Embarked'] = data['Embarked'].replace('Q',2)
data['Embarked'] = data['Embarked'].replace('S',3)

plt.figure(figsize=(12,8))
ax = sns.heatmap(data.corr().abs(), annot=True)
plt.show()
