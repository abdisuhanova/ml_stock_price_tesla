import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# Set seaborn style for better aesthetics
sb.set(style='whitegrid')

# Load the data
df = pd.read_csv('content/Tesla.csv')

# Clean dollar signs from relevant columns and convert them to numeric
for col in ['Close', 'Open', 'High', 'Low']:
    df[col] = df[col].str.replace('$', '', regex=True).astype(float)

# Parse the 'Date' column to datetime format and set it as the index
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')
df.set_index('Date', inplace=True)

# Check if data was loaded correctly (optional)
print(df.head())

# Plot the 'Close' prices
plt.figure(figsize=(15, 5))
plt.plot(df['Close'], color='blue', linewidth=2, label='Close Price')

# Add a title and labels
plt.title('Tesla Close Price', fontsize=18, fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Price in Dollars', fontsize=12)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Add gridlines for clarity
plt.grid(True, linestyle='--', alpha=0.7)

# Add a legend
plt.legend()

# Display the plot
plt.show()

