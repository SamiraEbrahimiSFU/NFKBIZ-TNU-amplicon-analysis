import pandas as pd

# File path
input_file = r"C:\Users\sea31\Desktop\sequence_trimmed.csv"

# Load the CSV file
df = pd.read_csv(input_file)

# Filter sequences that start with 'T' (uppercase)
starts_with_T = df[df['Sequence_in_between'].str.startswith('T', na=False)]

# Filter sequences that do NOT start with 'T'
not_start_with_T = df[~df['Sequence_in_between'].str.startswith('T', na=False)]

# Save outputs
output_with_T = r"C:\Users\sea31\Desktop\extracted_start_with_T.csv"
output_without_T = r"C:\Users\sea31\Desktop\extracted_not_start_with_T.csv"

starts_with_T.to_csv(output_with_T, index=False)
not_start_with_T.to_csv(output_without_T, index=False)

print(f"✅ Extracted files saved:\n- {output_with_T}\n- {output_without_T}")
