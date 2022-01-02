import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB

dataset = pd.read_csv("../datasheets/projection.csv")

cases = np.array(dataset.india.values.tolist()) # y
days = list(range(1, (len(cases) + 1))) # X
days = np.array([[day] for day in days])

days_pred = list(range(1, (len(cases) + 5)))
days_pred = np.array([[day] for day in days_pred])

clf = GaussianNB()
clf.fit(days, cases)
print(clf.predict(days_pred))
