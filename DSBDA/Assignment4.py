import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
x=np.array([95,85,80,70,60])
y=np.array([85,95,70,65,70])
model=np.polyfit(x,y,1)
# display(model)
predict=np.poly1d(model)
# predict(65)
y_pred=predict(x)
print(y_pred)

from sklearn.metrics import r2_score
r2_score(y,y_pred)

y_line = model[1]+model[0]*x
plt.plot(x,y_line,c='r')
plt.scatter(x,y_pred)
plt.scatter(x, y, c='r')

