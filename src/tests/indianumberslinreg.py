# now i know why data visualization is important
# explained why you should NEVER use linear regression in these cases

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv("../datasheets/projection.csv")

cases = np.array(dataset.india.values.tolist()).reshape(-1, 1)
days = np.array(list(range(1, (len(cases) + 1)))).reshape(-1, 1)

reg = LinearRegression().fit(days, cases)

y_pred = reg.predict(days)

plt.scatter(days, cases,  color='black')
plt.plot(days, y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()
