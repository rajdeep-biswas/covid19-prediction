import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import shutil
import datetime
from random import random

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Requets the JSON API and fetches the most recent data
response = requests.get('https://api.covid19india.org/data.json')

cases = []
dates = []

# Populates the two lists with timestamps and number of cumulative cases
for item in response.json()["cases_time_series"]:
    cases.append(int(item["totalconfirmed"]))
    dates.append(item["date"].strip())

filesavename = item["dateymd"]

# Looks at a third of the most recent cases for more accurate predictions
npastdates = len(dates) // 3
nfuturedates = 14

pdate = dates[-1]
dates = dates[:-1]

# Adds future dates for the output JSON.
for date in pd.date_range(pdate + str(datetime.now().year), periods=nfuturedates, freq='d'):
    dates.append(str(date.day) + " " + str(date.month_name()))

# Prepares X and y for prediction.
realcases = cases
cases = cases[-npastdates:]
days = list(range(len(cases)))

X = [[day] for day in days]
y = cases

X_pred = list(range(len(cases) + nfuturedates))
X_pred = [[x_pred] for x_pred in X_pred]

# Creates model and predicts following n day cases.

poly = PolynomialFeatures(4)

reg = LinearRegression().fit(poly.fit_transform(X), y)

y_pred = reg.predict(poly.fit_transform(X_pred))

# Prepares lists for writing into updates JSON file.

allcases = realcases
for item in y_pred[-nfuturedates:]:
    allcases.append(int(item))
    
datecases = []
for i in range(len(dates)):
    datecases.append([dates[i], allcases[i]])

jsondata = []
for item in [{"date": date, "totalconfirmed": confirmed} for [date, confirmed] in datecases]:
    jsondata.append(item)

jsondata = str({"cases_time_series" : jsondata}).replace("'", '"')
#print(y_pred)

# Writes into JSON file and creates a copy for backup.

with open("jsons/current.json", 'w') as f:
    f.write(json.dumps(json.loads(jsondata), indent=2, sort_keys=True))

shutil.copyfile("jsons/current.json", "jsons/" + filesavename + ".json")
