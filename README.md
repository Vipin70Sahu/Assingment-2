# Assignment: Overview of Famous Algorithms

## Author
Vipin Kumar Sahu (22111070)

## Date
October 24, 2024

## Introduction
This assignment provides an overview of several prominent machine learning algorithms, including Decision Trees, k-Nearest Neighbors (kNN), Support Vector Machines (SVM),
Linear Regression, and Logistic Regression. Each algorithm is discussed in terms of its definition, computational complexity, optimality, and completeness.

## Table of Contents
- [Introduction](#introduction)
- [Decision Tree](#decision-tree)
- [k-Nearest Neighbors (kNN)](#k-nearest-neighbors-knn)
- [Support Vector Machines (SVM)](#support-vector-machines-svm)
- [Linear Regression](#linear-regression)
- [Logistic Regression](#logistic-regression)
- [Conclusion](#conclusion)

## Decision Tree
A Decision Tree is a supervised learning algorithm used for classification and regression tasks.
It works by splitting the data into subsets based on the value of input features, creating a tree-like structure of decisions.

- Complexity: The time complexity is O(n log n) for training and O(log n) for prediction.
- Optimality: Decision Trees can overfit the training data, leading to suboptimal performance on unseen data.
- Completeness: They can represent any decision boundary but may require pruning to avoid overfitting.

## k-Nearest Neighbors (kNN)
k-Nearest Neighbors is a non-parametric, instance-based learning algorithm used for classification and regression. 
It classifies data points based on the majority class among the k-nearest neighbors in the feature space.

- Complexity: The time complexity for training is O(1), while for prediction, it is O(n) due to the need to calculate distances to all training examples.
- Optimality: kNN can achieve high accuracy but may struggle with large datasets due to its reliance on distance calculations.
- Completeness: It can approximate any decision boundary, but the choice of k can greatly affect performance.

## Support Vector Machines (SVM)
Support Vector Machines are supervised learning models used for classification and regression. 
SVMs work by finding the optimal hyperplane that maximizes the margin between different classes in the feature space.

- Complexity: The time complexity is O(n^2) to O(n^3) for training, depending on the implementation, while the prediction complexity is O(n).
- Optimality: SVMs are effective in high-dimensional spaces and are robust against overfitting,
- especially in cases where the number of dimensions exceeds the number of samples.
- Completeness: They can classify non-linearly separable data using kernel tricks.

## Linear Regression
Linear Regression is a supervised learning algorithm used for predicting a continuous target variable based on one or more predictor variables. 
It assumes a linear relationship between the input features and the target variable.

- Complexity: The time complexity for training is O(n^2) for the closed-form solution and O(n) for gradient descent, while prediction is O(n).
- Optimality: Linear Regression is optimal for datasets that exhibit linear relationships.
- Completeness: It can model only linear relationships, which may limit its applicability in certain scenarios.

## Logistic Regression
Logistic Regression is a statistical method used for binary classification that models the probability of a binary outcome based on one or more predictor variables. 
It uses the logistic function to transform the output.

- Complexity: The time complexity for training is O(n) for stochastic gradient descent and O(n^2) for the closed-form solution, while prediction is O(1).
- Optimality: Logistic Regression performs well with linearly separable data but may underperform with complex datasets.
- Completeness: It is suitable for binary classification but can be extended to multi-class problems using techniques like one-vs-all.

## Conclusion
This assignment provided an overview of various famous algorithms, discussing their definitions, computational complexities, optimality, and completeness. 
Understanding these algorithms is crucial for selecting the right model for specific data analysis tasks.

