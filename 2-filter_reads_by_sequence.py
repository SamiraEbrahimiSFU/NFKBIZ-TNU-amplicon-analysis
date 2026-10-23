from Bio import SeqIO
from Bio.Seq import Seq

# Input and output file paths
input_file = r"C:\Users\sea31\Desktop\Ctrl_R1_001_QC10plus.fasta"
output_file = r"C:\Users\sea31\Desktop\Filtered_sequences.fasta"

# Target sequence (forward)
target_seq = "GAAGAGCCTACGACGAC"

# Process reads
count_in = 0
count_out = 0

with open(output_file, "w") as out_handle:
    for record in SeqIO.parse(input_file, "fasta"):
        count_in += 1
        seq_str = str(record.seq).upper()
        rev_comp = str(Seq(target_seq).reverse_complement())

        if target_seq in seq_str or rev_comp in seq_str:
            SeqIO.write(record, out_handle, "fasta")
            count_out += 1

print(f"Filtering complete: {count_out} of {count_in} reads matched the target sequence.")
print("Output saved to:", output_file)
