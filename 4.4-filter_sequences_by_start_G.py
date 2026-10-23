import pandas as pd

# File path
input_file = r"C:\Users\sea31\Desktop\sequence_trimmed.csv"

# Load the CSV file
df = pd.read_csv(input_file)

# Filter sequences that start with 'G' (uppercase)
starts_with_G = df[df['Sequence_in_between'].str.startswith('G', na=False)]

# Filter sequences that do NOT start with 'G'
not_start_with_G = df[~df['Sequence_in_between'].str.startswith('G', na=False)]

# Save outputs
output_with_G = r"C:\Users\sea31\Desktop\extracted_start_with_G.csv"
output_without_G = r"C:\Users\sea31\Desktop\extracted_not_start_with_G.csv"

starts_with_G.to_csv(output_with_G, index=False)
not_start_with_G.to_csv(output_without_G, index=False)

print(f"✅ Extracted files saved:\n- {output_with_G}\n- {output_without_G}")
