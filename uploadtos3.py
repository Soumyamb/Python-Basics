import pandas as pd


df=pd.read_csv(r'Most Streamed Spotify Songs 2024.csv',sep=";", header=0, decimal=",")
#print(df.iloc[:,5:29])

for col in df.iloc[:,5:29]:
    if df[col].dtype == 'object':  # Check if the column type is object (string)
        df[col] = df[col].str.replace('.', ' ')
    # Display modified DataFrame
print("\nModified DataFrame:")
print(df)

# Define the path for the new CSV file
new_csv_file_path = 'path/to/your/new_output_file.csv'

# Save the DataFrame to a new CSV file
filename = 'Most Streamed Spotify Songs 2024 cleaned.csv'
df.to_csv(filename, index=False)  # Set index=False to avoid writing row numbers
print(f"DataFrame has been saved to {filename}")
