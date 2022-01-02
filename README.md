# COVID-19 India Daily Cases Prediction
**Update**: https://data.covid19india.org/data.json has stopped posting updates since 2021-08-16 (16th August, 2021) and hence the GitHub Actions Workflow has ceased to update this repository on its own as a result. Sorry for any inconvenience :(  
  
I will try to look into some alternatives as soon as I find some free time. *Thank you for visiting!*

## What does this do?
A simple Linear Regression model with a Polynomial features of degree 4 learn the data of last 30 days of growth of COVID-19 number of cases (cumulative) and try to predict what the following 15 days would look like.  
  
[View a live graph here](https://araon.github.io/Covid19-Dasboard/).  
  
⭐ The cool thing about this project - there is a GitHub Actions Workflow [configured](https://github.com/rajdeep-biswas/covid19-prediction/blob/master/.github/workflows/python-run.yaml)  in this repository that runs [`updatejson.py`](https://github.com/rajdeep-biswas/covid19-prediction/blob/master/pyfiles/updatejson.py) runs twice everyday to get the updated number of cases from a [Public Datasource API](https://data.covid19india.org/data.json), run the forecasting for the next 15 days and write it into a JSON file that gets committed back into this repo. And that is how the above webpage gets updated everyday without requiring any backend. ;)  
  
There is a bunch of other code and files on this repo that are not directly related to this usecase. I have only left them here due to preservation reasons. *Delve at your own risk*!