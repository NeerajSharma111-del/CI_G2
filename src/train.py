import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

X =np.random.rand(100,1)
y=2*X+1

model = LinearRegression()
model.fit(X,y)

joblib.dump(model,'src/model.pkl')
print("Model training complete")