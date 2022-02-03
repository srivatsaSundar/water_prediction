import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

water = pd.read_csv("water_potability.csv")

water["ph"].fillna(value=water["ph"].mean(), inplace=True)
water["Trihalomethanes"].fillna(value=water["Trihalomethanes"].mean(), inplace=True)
water["Sulfate"].fillna(value=water["Sulfate"].mean(), inplace=True)


x=water.drop("Potability",axis=1)
y=water.Potability


# Initiatlize the model
logreg = LogisticRegression(solver='liblinear', random_state = 0)

# Fit the model
logreg.fit(x, y)  

pickle.dump(logreg, open('ml_model.pkl', 'wb'))  