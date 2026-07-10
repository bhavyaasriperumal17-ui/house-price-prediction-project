import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Sample data
X = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
y = [10, 20, 30]

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
pickle.dump(model, open('model.pkl', 'wb'))

print("model saved")
