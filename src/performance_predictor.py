import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pytest

# Sample student data (grades and study hours)
data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Study Hours': [10, 20, 30, 40, 50],
    'Grades': [85, 88, 90, 92, 95]
}

# Create DataFrame
df = pd.DataFrame(data)

# Visualize the data
def visualize_data(df):
    plt.scatter(df['Study Hours'], df['Grades'])
    plt.xlabel('Study Hours')
    plt.ylabel('Grades')
    plt.title('Study Hours vs Grades')
    plt.show()

# Train a model to predict grades based on study hours
def predict_grades(df):
    X = df[['Study Hours']]  # Features
    y = df['Grades']  # Target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    print(f'Mean Squared Error: {mse}')
    return model

# Test the predict_grades function
def test_predict_grades():
    model = predict_grades(df)
    assert model is not None

if __name__ == "__main__":
    visualize_data(df)
    model = predict_grades(df)
    test_predict_grades()
