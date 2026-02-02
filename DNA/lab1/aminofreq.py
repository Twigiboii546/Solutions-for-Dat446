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
    rdict = {}
    for codon in codons:
        if codon in genetic_code:
            aa = genetic_code[codon] #skapar alla nycklar 
            if aa in rdict:
                rdict[aa] += 1 #utökar med 1 om den finns i codon
            if aa not in rdict:
                rdict[aa] = 1 

                
    return rdict

def read_dna(identifier, filepath):
    result = ""
    reading = False
    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()

            if line == "":
                continue
            if line[0] == ">":
                if reading == True:
                    break
                reading = (line[i:] == identifier)
                continue
            if reading:
                result += line.upper()
    return result
        

            
#print(aa_count(["ATG","GTG","GTC","TAG"], {'ATG':'M','TTT':'F','TTC':'F','GTC':'V','GTG':'V','AAC':'N','TAT':'Y'}))
print(read_dna('sequence1','examples/example1.fna'))



#def composition(identifier,filepath,genetic_code,start_codons,stop_codons):


#print(codons_extract("abcDEdfaksdasdads",1))



