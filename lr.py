from sklearn.linear_model import LinearRegression
import numpy as np

# Example data
X = np.array([[1, 1], [2, 2], [3, 3], [4, 4]])
y = np.array([2, 3, 4, 5])

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Make predictions
predictions = model.predict(np.array([[5, 5]]))
print(predictions)