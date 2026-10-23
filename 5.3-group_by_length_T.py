import pandas as pd
import matplotlib.pyplot as plt
import os

# Path to your input CSV
input_file = 'extracted_not_start_with_T_clean_Up.csv'

# Load CSV
df = pd.read_csv(input_file)

# Group by length and sum the counts
grouped = df.groupby('Length')['Count'].sum().reset_index()

# Save output Excel file to desktop
desktop_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'Grouped_Read_Counts.xlsx')
grouped.to_excel(desktop_path, index=False)

# Plot
plt.figure()
plt.bar(grouped['length'], grouped['Count'])
plt.xlabel('Sequence Length')
plt.ylabel('Total Read Count')
plt.title('Read Count per Sequence Length')
plt.tight_layout()
plt.show()
