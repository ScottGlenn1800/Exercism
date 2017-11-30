def to_rna(dna_strand):
    rna_strand = []
    translation = {"G":"C","C":"G","T":"A","A":"U"}
    for nucleotides in dna_strand:
        try:
            rna_strand.append(translation[nucleotides])
        except KeyError:
            raise ValueError("ERROR! Please use the appropriate DNA Nucleotides: G, C, T, or A.")
    string = ""
    for nucleotide in rna_strand:
        string = string + nucleotide
    return string