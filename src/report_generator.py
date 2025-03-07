import pandas as pd

# Generate a performance report for each student
def generate_report(df):
    for index, row in df.iterrows():
        report = f"Performance Report for {row['Student Name']}:\n"
        report += f"Average Grade: {row['average_grade']:.2f}\n"
        report += "Subject-wise Grades:\n"
        report += f"  Subject 1: {row['Subject 1 Grade']}\n"
        report += f"  Subject 2: {row['Subject 2 Grade']}\n"
        report += f"  Subject 3: {row['Subject 3 Grade']}\n"
        report += "----------------------------------------\n"
        
        print(report)
        # You can save the reports to a file if required.
        # with open(f"reports/{row['Student Name']}_report.txt", "w") as f:
        #     f.write(report)
