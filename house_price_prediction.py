import pandas as pd

#load dataset
url = "https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv"
dataset = pd.read_csv(url)

# View the first few rows
print(dataset.head())