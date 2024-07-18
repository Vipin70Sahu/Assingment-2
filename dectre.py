from sklearn.tree import DecisionTreeClassifier
import numpy as np

# Ex
X = np.array([[1, 1], [2, 2], [3, 3], [4, 4]])
y = np.array([0, 0, 1, 1])

# Create and train
model = DecisionTreeClassifier()
model.fit(X, y)

# Make predictions
predictions = model.predict(np.array([[1.5, 1.5]]))
print(predictions)