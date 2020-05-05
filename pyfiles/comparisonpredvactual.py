# confirmed - recovered - deaths is a better idea since i.e the active number of cases

import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import shutil
from random import random

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

response = requests.get('https://api.covid19india.org/data.json')
oldjson = json.load(open("../jsons/2020-4-15.json", "r"))

predictedcases = []
predicteddates = []
for item in oldjson["India"]:
    predictedcases.append(item["confirmed"])
    predicteddates.append(item["date"])

actualcases = []
actualdates = []
for item in response.json()["cases_time_series"]:
    actualcases.append(int(item["totalconfirmed"]))
    actualdates.append(item["date"].strip())

predictedcases = predictedcases[8:]
#actualcases = actualcases[:len(predictedcases)]
days = list(range(len(predictedcases)))

#predicteddates = predicteddates[8:]
#actualdates = actualdates[:len(predicteddates) - 2]

plt.plot(days, predictedcases, 'r')
plt.plot(days, actualcases)
plt.show()
