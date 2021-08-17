import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
df = pd.read_csv("Home_prices.csv")

# How to handle NaN value in Bedrooms column: To take median of that column
# I need integers value so,I import math module
median_Bedrooms = math.floor(df["Bedrooms"].median())

df["Bedrooms"] = df["Bedrooms"].fillna(median_Bedrooms)
X = df.drop(["Price"],axis =1)
y =df["Price"]

# Lets train our model
model = LinearRegression().fit(X,y)
print(model)
y_p =model.predict([[2600,3,20]])
print(y_p)

# Lets calculate the efficiency of the model
model_eff = model.score(X,y)
print(model_eff)

# Lets save the model
import pickle
with open("Home_prices.pkl","wb") as file :
    pickle.dump(model,file)
with open("Home_prices.pkl","rb") as f:
    model = pickle.load(f)
print(model)