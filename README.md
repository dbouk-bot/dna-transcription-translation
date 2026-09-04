# dna-transcription-translation
This code is meant to take in user-inputed DNA sequences and convert it into a chain of amino acids. I built this code to both practice python and to give me a basic understanding of what the bioinformatics field is like. 

# how the code works
- the code asks the user for a DNA sequence, and makes sure that the user only uses the letters 'AUG'
- will then convert the DNA into RNA (replace T wth A)
- it then scans the sequence for the start codon (AUG) and will cut off the letter form that come before it and section the rest of the sequence into codons(groups of 3 letters) using regex
- afterwards it replaces each codon with its respective amino acid using a dictionary, and will stop once it reaches a stop codon
