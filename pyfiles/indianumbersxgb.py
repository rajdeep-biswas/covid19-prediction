# confirmed - recovered - deaths is a better idea since i.e the active number of cases

import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import shutil
from random import random

from xgboost import XGBRegressor, DMatrix
from sklearn.model_selection import train_test_split

response = requests.get('https://pomber.github.io/covid19/timeseries.json')

npastdates = 20
nfuturedates = 20

cases = []
dates = []
for item in response.json()["India"]:
    cases.append(item["confirmed"])
    dates.append(item["date"])

pdate = dates[-1]

for date in pd.date_range(pdate, periods=nfuturedates, freq='d'):
    [y, m, d] = str(date)[:10].split("-")
    if m[0] == '0':
	    m = m[-1]
    if d[0] == '0':
	    d = d[-1]
    dates.append(y + "-" + m + "-" + d)

realcases = cases
#cases = cases[-npastdates:]
days = list(range(len(cases)))

X = [[day] for day in days]
y = cases

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=2)

X_pred = list(range(len(cases) + nfuturedates))
X_pred = [[x_pred] for x_pred in X_pred]

#dtrain = DMatrix(data=X, label=y)

reg = XGBRegressor()#n_estimators=10, max_depth=3)#, learning_rate=0.03)
reg = reg.fit(np.array(X_train), y_train)

y_pred = reg.predict(np.array(X_test))

print(pd.DataFrame(y_pred, y_test))

#plt.scatter(X, y,  color='black')
#plt.plot(X, y_pred, color='blue', linewidth=2)

plt.xticks(())
plt.yticks(())

#allcases = realcases
#for item in y_pred[-20:]:
#    allcases.append(int(item))
    
#datecases = []
#for i in range(len(dates)):
#    datecases.append([dates[i], allcases[i]])

#jsondata = []
#for item in [{"date": date, "confirmed": confirmed} for [date, confirmed] in datecases]:
#    jsondata.append(item)

#jsondata = str({"India" : jsondata}).replace("'", '"')
#print(y_pred)

#with open("../jsons/current.json", 'w') as f:
#    f.write(json.dumps(json.loads(jsondata), indent=2, sort_keys=True))

#shutil.copyfile("../jsons/current.json", "../jsons/" + pdate + ".json")
#savepath = "../plots/" + str(round(random() * 100000)) + ".png"
#plt.savefig(savepath)
#plt.show()
