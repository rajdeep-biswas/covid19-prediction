# confirmed - recovered - deaths is a better idea since i.e the active number of cases

import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from random import random

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

response = requests.get('https://pomber.github.io/covid19/timeseries.json')

cases = []
for item in response.json()["India"]:
    cases.append(item["confirmed"])

days = list(range(len(cases)))

X = [[day] for day in days]
y = cases

X_pred = list(range(len(cases) + 20))
X_pred = [[x_pred] for x_pred in X_pred]

poly = PolynomialFeatures(6)

reg = LinearRegression().fit(poly.fit_transform(X), y)

y_pred = reg.predict(poly.fit_transform(X_pred))

plt.scatter(X, y,  color='black')
plt.plot(X_pred, y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

#print(y_pred)
#for item in y_pred:
#    print(item)

#savepath = "../plots/" + str(round(random() * 100000)) + ".png"
#plt.savefig(savepath)
plt.show()

