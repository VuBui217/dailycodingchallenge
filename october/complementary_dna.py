"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-25

Complementary DNA
Given a string representing a DNA sequence, return its complementary strand using the following rules:

DNA consists of the letters "A", "C", "G", and "T".
The letters "A" and "T" complement each other.
The letters "C" and "G" complement each other.
For example, given "ACGT", return "TGCA".
"""

def complementary_dna(strand):
    dna_map = {'A': 'T', 'T': 'A', 'C': 'G', 'G':'C'}
    return ''.join(dna_map[ch] for ch in strand)


# complementary_dna("ACGT")                 # should return "TGCA".
# complementary_dna("ATGCGTACGTTAGC")       # should return "TACGCATGCAATCG".
# complementary_dna("GGCTTACGATCGAAG")      # should return "CCGAATGCTAGCTTC".
# complementary_dna("GATCTAGCTAGGCTAGCTAG") # should return "CTAGATCGATCCGATCGATC".
