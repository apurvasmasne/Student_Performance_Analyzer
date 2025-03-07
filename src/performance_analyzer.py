import pandas as pd
import matplotlib.pyplot as plt
from report_generator import generate_report
from performance_predictor import predict_performance

# Load the student grades data
def load_data(file_path):
    return pd.read_csv(file_path)

# Analyze student performance
def analyze_performance(df):
    # Calculate average grade for each student
    df['average_grade'] = df.iloc[:, 1:-1].mean(axis=1)
    return df

# Generate a performance report
def generate_performance_report(df):
    generate_report(df)

# Visualize performance data
def visualize_performance(df):
    # Generate histograms and bar charts
    plt.hist(df['average_grade'], bins=10, color='blue', edgecolor='black')
    plt.title('Distribution of Average Grades')
    plt.xlabel('Average Grade')
    plt.ylabel('Frequency')
    plt.show()

def main():
    file_path = 'data/student_grades.csv'  # Path to the data file
    df = load_data(file_path)
    df = analyze_performance(df)
    print(df)

    # Visualize data
    visualize_performance(df)

    # Predict performance trends
    predicted_performance = predict_performance(df)
    print(f"Predicted performance trends: {predicted_performance}")

    # Generate report
    generate_performance_report(df)

if __name__ == "__main__":
    main()
