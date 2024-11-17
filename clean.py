import pandas as pd

# 1. Load the dataset from Tesla.csv
df = pd.read_csv('Tesla.csv')
print("Original Data (First 5 Rows):")
print(df.head())

# 2. Convert 'Date' to datetime and remove dollar signs
df['Date'] = pd.to_datetime(df['Date'])
for col in ['Close', 'Open', 'High', 'Low']:
    df[col] = df[col].str.replace('$', '', regex=False).astype(float)

print("\nData After Cleaning Data Types:")
print(df.head())

# 3. Check for missing values
print("\nMissing Values per Column:")
print(df.isnull().sum())

# 4. Remove duplicates
df_cleaned = df.drop_duplicates()
print("\nData After Removing Duplicates:")
print(df_cleaned.head())

# 5. Detect and handle outliers (remove values beyond 99th percentile)
numeric_cols = ['Close', 'Open', 'High', 'Low', 'Volume']
for col in numeric_cols:
    upper_limit = df_cleaned[col].quantile(0.99)
    df_cleaned = df_cleaned[df_cleaned[col] <= upper_limit]

print("\nData After Outlier Removal:")
print(df_cleaned.head())

# 6. Save the cleaned data to a new CSV file
df_cleaned.to_csv('cleaned.csv', index=False)
print("\nCleaned Data saved as 'Cleaned_Tesla.csv'.")
