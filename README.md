NFKBIZ-TNU Amplicon Sequencing Analysis

Overview:

This repository contains custom Python scripts for analyzing Amplicon-EZ high-throughput sequencing data from the NFKBIZ 3′UTR target region (TNU). The analysis characterizes cleavage-site heterogeneity and non-templated nucleotide additions, including uridylation, in sequencing reads derived from NFKBIZ 3′UTR cleavage products.

Analysis workflow

The scripts perform the following steps:

Quality filtering: Retain sequencing reads with a minimum Phred quality score of 10 at all positions.

Read selection: Identify reads containing the ligated adenylated oligonucleotide or its reverse complement.

Target extraction: Extract the intervening sequence spanning the NFKBIZ TNU target region.

Cleavage-site analysis: Sequentially compare reads with the expected endogenous sequence to identify cleavage-site heterogeneity.

Non-templated addition analysis: Identify nucleotide additions that differ from the expected sequence, including uridine extensions.

Quantification: Calculate extension lengths and read counts and determine the nucleotide composition (A, U, G, and C) at the main cleavage site.

Requirements:

Python 3

Biopython

Install Biopython using:

pip install biopython

Input data

The analysis uses Amplicon-EZ sequencing reads generated from PCR-amplified NFKBIZ 3′UTR cleavage products. Input files should be provided in the format expected by the analysis scripts.

Usage:

Download or clone this repository.

Install the required Python dependencies.

Place the sequencing data in the appropriate input directory or update the input file paths in the scripts.

Run the relevant Python script(s).


Data availability

Raw sequencing data are deposited in the NCBI Sequence Read Archive (SRA) under BioProject accession: [SUB16583568].
