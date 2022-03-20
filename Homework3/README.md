Homework Details:

Build multiple classifiers for the Breast Cancer Wisconsin dataset of UCI. In this homework, you need to download breast cancer dataset from UCI web site, perform
Exploratory Data Analysis on the dataset and build multiple models using different algorithms on the dataset to predict whether a patient has breast cancer or not.

Details:
- Obtain the data from UCI website. You should use the original data, do not use any other curated or cleaned data, or data from sklearn or other libraries.

http://archive.ics.uci.edu/ml/datasets/breast+cancer+wisconsin+%28diagnostic%29

** Data file is named wdbc.data and its description is in wdbc.names.

Exploratory Data Analyis: Play with the data, look for null values, find correlations between features, use scaling/standardization on data.
- Check for null values
- Plot correlation heatmap of features
- Plot class labels, check if there is imbalance
- Apply scaling/standardization on features
- Pairplots


After your changes on your data, save it as "data.csv". You will submit this file with your homework.

Split the dataset into training-set and test-set (X_train, X_test)
- Hint: You can use library functions to split data

Build multiple models and train them using the following methods/algorithms (you can use libraries like sklearn, etc.):
- SVM - Support Vector Machines
- Logistic Regression
- Random Forest
- Decision Tree
- KNeighborsClassifier

Test your models on test data and calculate confusion matrix, accuracy,precision, recall, f1-score for each model. Print the confusion matrix, accuracy, precision, recall, f1-score.

For each model, print the indices of data those are misclassified by each model (False-positive, false-negative)

Which of the 5 models performed well? What do you think about the best-model’s performance on this data? Write a paragraph about your findings.