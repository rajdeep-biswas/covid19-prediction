# the only one that works

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from random import random

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv("../datasheets/projection.csv")

y = np.array(dataset.india.values.tolist()) # y
X = list(range(1, (len(y) + 1))) 
X = np.array([[x] for x in X]) # X

X_pred = list(range(1, (len(y) + 10)))
X_pred = np.array([[x_pred] for x_pred in X_pred])

poly = PolynomialFeatures(3)

reg = LinearRegression().fit(poly.fit_transform(X), y)

y_pred = reg.predict(poly.fit_transform(X_pred))

plt.scatter(X, y,  color='black')
plt.plot(X_pred, y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

print(y_pred)

#savepath = "../plots/" + str(round(random() * 100000)) + ".png"
#plt.savefig(savepath)
plt.show()
