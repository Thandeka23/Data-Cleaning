import pandas as pd
import numpy as np

# Step 1: Load the data
# Specify the correct path to your CSV file
df = pd.read_csv(r'C:\Users\CAPACITI-JHB\StudentPerformanceFactors.csv')

# Perform basic cleaning of the dataset:
print("Dataset Info:")
print(df.info())
print("\nFirst few rows:")
print(df.head()) # View the first few rows of df

# Step 2: Remove or handle missing values.
print("\nMissing values:")
print(df.isnull().sum())

# Handle missing values
# For numeric columns, we'll fill with median. For categorical, we'll fill with mode.
for column in df.columns:
    if df[column].dtype == 'object':
        df[column] = df[column].fillna(df[column].mode()[0])
    else:
       df[column] = df[column].fillna(df[column].median())

# Step 3:Correct data types where necessary.
# Convert numeric columns to appropriate types
numeric_columns = ['Hours_Studied', 'Attendance', 'Previous_Scores', 'Sleep_Hours', 'Tutoring_Sessions', 'Physical_Activity', 'Distance_from_Home', 'Exam_Score']
for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Step 4: Eliminate any irrelevant column.
# For this dataset we will remove the irrelevant 'Distance_from_Home' column
df = df.drop('Distance_from_Home', axis=1) 
print("\nCleaned Dataset Info:")   # Display the cleaned dataset info
print(df.info())

# Step 5: Check for and remove duplicates
duplicates = df.duplicated().sum()
print(f"\nNumber of duplicate rows: {duplicates}")
df.drop_duplicates(inplace=True)

# Step 7: Display summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Step 8: Save the cleaned dataset
df.to_csv('cleaned_StudentPerformanceFactors.csv', index=False)
print("\nCleaned dataset saved as 'cleaned_StudentPerformanceFactors.csv'")