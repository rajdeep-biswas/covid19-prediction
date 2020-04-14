import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

dataset = pd.read_csv("../datasheets/IndividualDetails.csv")

# replacing all NaNs with means in the age column
dataset["age"].fillna(dataset["age"].mean(), inplace = True)

# categorizing genders into M, F and NA
dataset["gender"] = pd.Categorical(dataset["gender"]).codes

# categorizing detected_city, detected_district, detected_state and nationality
dataset["detected_city"] = pd.Categorical(dataset["detected_city"]).codes
dataset["detected_district"] = pd.Categorical(dataset["detected_district"]).codes
dataset["detected_state"] = pd.Categorical(dataset["detected_state"]).codes
dataset["nationality"] = pd.Categorical(dataset["nationality"]).codes

dataset = dataset[["age", "gender", "detected_city", "detected_district", "detected_state", "nationality"]]

kmeans = KMeans(n_clusters=4)
kmeans.fit(dataset)
kmeans.cluster_centers_
