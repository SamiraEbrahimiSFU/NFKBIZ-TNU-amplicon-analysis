from collections import defaultdict
from Bio import SeqIO
from Bio.Seq import Seq

# Input FASTA file
input_file = r"C:\Users\sea31\Desktop\Filtered_sequences.fasta"

# Motifs
start_motif = "GAGCCT"
end_motif = "GAAGAGCCTA"

# Dictionary to store sequences and counts
seq_counts = defaultdict(int)

def extract_between(seq, is_reverse=False):
    """Extract sequence between motifs, return '0' if adjacent, or None if not found."""
    if start_motif in seq and end_motif in seq:
        start_idx = seq.find(start_motif) + len(start_motif)
        end_idx = seq.find(end_motif)
        if start_idx < end_idx:
            return seq[start_idx:end_idx]
        elif start_idx == end_idx:
            return "0"
    return None

# Read FASTA file
for record in SeqIO.parse(input_file, "fasta"):
    seq_fwd = str(record.seq)
    seq_rev = str(record.seq.reverse_complement())

    # Forward strand
    result_fwd = extract_between(seq_fwd)
    if result_fwd is not None:
        seq_counts[result_fwd] += 1

    # Reverse strand
    result_rev = extract_between(seq_rev, is_reverse=True)
    if result_rev is not None:
        seq_counts[result_rev] += 1

# Write output summary
with open(r"C:\Users\sea31\Desktop\extracted_summary.csv", "w") as out:
    out.write("Sequence_in_between,Count,Length\n")
    for seq, count in seq_counts.items():
        length = 0 if seq == "0" else len(seq)
        out.write(f"{seq},{count},{length}\n")

print("✅ Done! Results (including reverse strands) saved to 'extracted_summary.csv' on Desktop.")
