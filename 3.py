import pandas as pd

df = pd.read_csv("C:\\Users\\sikri\\OneDrive\\Documents\\car_sales.csv", encoding="latin-1")

print("display the info of dataset")
print(df)
print(df.describe())