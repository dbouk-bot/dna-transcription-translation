import re
rna = []

while True:
    seq = input("Enter a DNA sequence: ").upper()
    if len(seq) < 15:
        print("Sequence too short, must be at least 15 characters")
        continue

    elif any(i not in ('A', 'T', 'G', 'C') for i in seq):
        print("Invalid character found, only A, T, G, C are allowed.")
        continue
    else:
        print("Valid DNA sequence entered.")
        break


if True:
    print("Converting DNA to RNA...")
    for i in seq:
        if i == 'A':
            rna.append('U')
        elif i == 'T':
            rna.append('A')
        elif i == 'G':
            rna.append('C')
        elif i == 'C':
            rna.append('G')
    print("RNA sequence:", ''.join(rna))

amino_acid = {'UUU': 'Phenylalanine', 'UUC': 'Phenylalanine', 'UUA': 'Leucine', 'UUG': 'Leucine',
              'CUU': 'Leucine', 'CUC': 'Leucine', 'CUA': 'Leucine', 'CUG': 'Leucine', 'AUU': 'Isoleucine', 'AUC': 'Isoleucine', 'AUA': 'Isoleucine', 'AUG': 'Methionine', 'GUU': 'Valine', 'GUC': 'Valine', 'GUA': 'Valine', 'GUG': 'Valine', 'UCU': 'Serine', 'UCC': 'Serine', 'UCA': 'Serine', 'UCG': 'Serine', 'CCU': 'Proline', 'CCC': 'Proline', 'CCA': 'Proline', 'CCG': 'Proline', 'ACU': 'Threonine', 'ACC': 'Threonine', 'ACA': 'Threonine', 'ACG': 'Threonine', 'GCU': 'Alanine', 'GCC': 'Alanine', 'GCA': 'Alanine', 'GCG': 'Alanine', 'UAU': 'Tyrosine', 'UAC': 'Tyrosine', 'UAA': 'Stop', 'UAG': 'Stop', 'UGA': 'Stop', 'CAU': 'Histidine', 'CAC': 'Histidine', 'CAA': 'Glutamine', 'CAG': 'Glutamine', 'AAU': 'Asparagine', 'AAC': 'Asparagine', 'AAA': 'Lysine', 'AAG': 'Lysine', 'GAU': 'Aspartic acid', 'GAC': 'Aspartic acid', 'GAA': 'Glutamic acid', 'GAG': 'Glutamic acid', 'UGU': 'Cysteine', 'UGC': 'Cysteine', 'UGG': 'Tryptophan', 'UGA': 'Stop', 'CGU': 'Arginine', 'CGC': 'Arginine', 'CGA': 'Arginine', 'CGG': 'Arginine', 'AGU': 'Serine', 'AGC': 'Serine', 'AGA': 'Arginine', 'AGG': 'Arginine', 'GGU': 'Glycine', 'GGC': 'Glycine', 'GGA': 'Glycine', 'GGG': 'Glycine'}


start_codon = re.search('AUG', ''.join(rna))

if start_codon is None:
    print("No start codon found.")
else:
    print(start_codon)
    newrna = ''.join(rna)[start_codon.start():]

print(newrna)
match = re.compile("[A-Z]{3}")
codon = match.findall(newrna)
print(codon)


for i in codon:
    print(amino_acid[i])
    if amino_acid[i] == 'Stop':
        print("stop codon has been reached")
        break
