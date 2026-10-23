import pandas as pd

# File path
input_file = r"C:\Users\sea31\Desktop\sequence_trimmed.csv"

# Load the CSV file
df = pd.read_csv(input_file)

# Filter sequences that start with 'A' (uppercase)
starts_with_A = df[df['Sequence_in_between'].str.startswith('A', na=False)]

# Filter sequences that do NOT start with 'A'
not_start_with_A = df[~df['Sequence_in_between'].str.startswith('A', na=False)]

# Save outputs
output_with_A = r"C:\Users\sea31\Desktop\extracted_start_with_A.csv"
output_without_A = r"C:\Users\sea31\Desktop\extracted_not_start_with_A.csv"

starts_with_A.to_csv(output_with_A, index=False)
not_start_with_A.to_csv(output_without_A, index=False)

print(f"✅ Extracted files saved:\n- {output_with_A}\n- {output_without_A}")
