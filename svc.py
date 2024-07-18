from sklearn.svm import SVC
import numpy as np

# Example data
X = np.array([[1, 1], [2, 2], [3, 3], [4, 4]])
y = np.array([0, 0, 1, 1])

# Create and train the model
model = SVC()
model.fit(X, y)

# Make predictions
predictions = model.predict(np.array([[2.5, 2.5]]))
print(predictions)