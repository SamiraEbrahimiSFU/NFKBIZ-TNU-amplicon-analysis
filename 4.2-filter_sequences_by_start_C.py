import pandas as pd

# File path
input_file = r"C:\Users\sea31\Desktop\sequence_trimmed.csv"

# Load the CSV file
df = pd.read_csv(input_file)

# Filter sequences that start with 'C' (uppercase)
starts_with_C = df[df['Sequence_in_between'].str.startswith('C', na=False)]

# Filter sequences that do NOT start with 'C'
not_start_with_C = df[~df['Sequence_in_between'].str.startswith('C', na=False)]

# Save outputs
output_with_C = r"C:\Users\sea31\Desktop\extracted_start_with_C.csv"
output_without_C = r"C:\Users\sea31\Desktop\extracted_not_start_with_C.csv"

starts_with_C.to_csv(output_with_C, index=False)
not_start_with_C.to_csv(output_without_C, index=False)

print(f"✅ Extracted files saved:\n- {output_with_C}\n- {output_without_C}")
