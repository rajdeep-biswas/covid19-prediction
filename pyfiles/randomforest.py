import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

dataset = pd.read_csv("../datasheets/COVID19_line_list_data.csv")

# replacing all NaNs with means in the age column
dataset["age"].fillna(dataset["age"].mean(), inplace = True)

# categorizing genders into M, F and NA
dataset["gender"] = pd.Categorical(dataset["gender"]).codes

# categorizing detected_city, detected_district, detected_state and nationality
dataset["location"] = pd.Categorical(dataset["location"]).codes
dataset["country"] = pd.Categorical(dataset["country"]).codes
dataset["death"] = pd.Categorical(dataset["death"]).codes

X = dataset[["age", "gender", "location", "country"]].values
y1 = dataset[["death"]].values

y = []
for i in range(len(y1)):
    if y1[i][0] == 0:
        y.append(0)
    else:
        y.append(1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)

clf = RandomForestClassifier(max_depth=2, random_state=0)
clf.fit(X_train, y_train)
print(clf.feature_importances_)
y_pred = clf.predict([[0, 0, 0, 0]])

print("Number of mislabeled points out of a total %d points : %d" % (X_test.shape[0], (y_test != y_pred).sum()))
print("Accuracy: " + str(100 - (y_test != y_pred).sum() / X_test.shape[0] * 100) + '%')
