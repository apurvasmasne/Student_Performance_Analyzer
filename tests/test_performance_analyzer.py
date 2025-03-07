
import pytest
import pandas as pd
from src.performance_analyzer import analyze_performance
from src.performance_predictor import predict_performance

# Sample data for testing
test_data = {
    'Student Name': ['John Doe', 'Jane Smith', 'Emily Davis', 'Michael Brown', 'Sarah Lee'],
    'Subject 1 Grade': [85, 88, 75, 92, 80],
    'Subject 2 Grade': [78, 84, 80, 95, 83],
    'Subject 3 Grade': [92, 90, 70, 93, 85],
    'Final Grade': [85, 87, 75, 93, 83]
}
df = pd.DataFrame(test_data)

def test_analyze_performance():
    df_analyzed = analyze_performance(df)
    assert df_analyzed['average_grade'].iloc[0] == pytest.approx(85.0, 0.1)

def test_predict_performance():
    predicted_performance = predict_performance(df)
    assert len(predicted_performance) == 1  # There will be one predicted value per test set
