import pandas as pd

# Read the CSV file
df = pd.read_csv('pokemon_complete_data.csv')

# Print the original number of rows
print(f"Original number of rows: {len(df)}")

# Remove duplicates based on the 'Name' column, keeping the first occurrence
df_no_duplicates = df.drop_duplicates(subset='Name', keep='first')

# Print the number of rows after removing duplicates
print(f"Number of rows after removing duplicates: {len(df_no_duplicates)}")

# Save the deduplicated data to a new CSV file
df_no_duplicates.to_csv('pokemon_data_no_duplicates.csv', index=False)

print("Deduplicated data saved to 'pokemon_data_no_duplicates.csv'")

# Create a separate CSV with only the duplicates
duplicates = df[df.duplicated(subset='Name', keep=False)]
duplicates.to_csv('pokemon_duplicates.csv', index=False)
print("Duplicate entries saved to 'pokemon_duplicates.csv'")