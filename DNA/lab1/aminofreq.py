
from aminofreq import *



def codons_extract(dna, frame):
    rlist = []
    dnacut = dna[frame:].upper()
    for i in range(len(dnacut)):
        if i % 3 == 0:
            rlist.append(dnacut[i-3:i])
    return rlist




def protein_extract(codons, start_codons, stop_codons):
    rlist = []
    for codon in codons:
        if codon == start_codons:
            rlist.append(codon)
            for codon2 in codons:
                if codon2 == stop_codons:
                    rlist.append(codon2)
    return rlist



def aa_count(codons, genetic_code):


    




#def read_dna(identifier, filepath):


#def composition(identifier,filepath,genetic_code,start_codons,stop_codons):


#print(codons_extract("abcDEdfaksdasdads",1))



