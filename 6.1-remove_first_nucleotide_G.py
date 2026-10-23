import pandas as pd

# File path
input_file = r"C:\Users\sea31\Desktop\extracted_start_with_G.csv"  
output_file = r"C:\Users\sea31\Desktop\sequence_trimmed.csv"

# Load the CSV file
df = pd.read_csv(input_file)

# Clean column names
df.columns = df.columns.str.strip()

# Apply changes: Remove first nucleotide, adjust Length
df['Sequence_in_between'] = df['Sequence_in_between'].str[1:]
df['Length'] = df['Length'] - 1

# Save the updated file
df.to_csv(output_file, index=False)

print(f"✅ Updated file saved to: {output_file}")
