import seaborn as sns
import matplotlib.pyplot as plt
dataset = sns.load_dataset('iris')
dataset.head()

fig, axes = plt.subplots(2,2,figsize=(16,9))
sns.histplot(dataset['sepal_length'], ax=axes[0,0])
sns.histplot(dataset['sepal_width'], ax=axes[0,1])
sns.histplot(dataset['petal_length'], ax=axes[1,0])
sns.histplot(dataset['petal_width'], ax=axes[1,1])

fig, axes = plt.subplots(2,2,figsize=(16,9))
sns.boxplot(y="petal_length", x="species", data=dataset, ax=axes[0,0])
sns.boxplot(y="petal_width", x="species", data=dataset, ax=axes[0,1])
sns.boxplot(y="sepal_length", x="species", data=dataset, ax=axes[1,0])
sns.boxplot(y="sepal_width", x="species", data=dataset, ax=axes[1,1])