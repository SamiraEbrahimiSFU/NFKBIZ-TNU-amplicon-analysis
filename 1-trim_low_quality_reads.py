from Bio import SeqIO

# Input and output file paths
input_file = r"C:\Users\sea31\Desktop\Ctrl_R1_001.fastq"
output_file = r"C:\Users\sea31\Desktop\Ctrl_R1_001_QC10plus.fastq"

# Quality threshold
quality_threshold = 10


# Process reads
with open(output_file, "w") as out_handle:
    count_in = 0
    count_out = 0
    for record in SeqIO.parse(input_file, "fastq"):
        count_in += 1
        if min(record.letter_annotations["phred_quality"]) >= quality_threshold:
            SeqIO.write(record, out_handle, "fastq")
            count_out += 1

print(f"Filtering complete: {count_out} of {count_in} reads passed (all Q ≥ {quality_threshold}).")
print("Output saved to:", output_file)
