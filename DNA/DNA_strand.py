def DNA_strand(dna):
    # code here
    def options(i):
        switcher={
            'A':'T',
            'T':'A',
            'G':'C',
            'C':'G'
            }
        return switcher.get(i)
    poli = []
    for l in dna:
        poli.append(options(l))
    new_dna = str(poli).replace(',', '')
    new_dna = str(new_dna).replace("'",'')
    new_dna = str(new_dna).replace(" ",'').replace("[",'').replace(']','')
    return new_dna






DNA_strand("AAAA")  #,"TTTT","String AAAA is")
DNA_strand("ATTGC") #,"TAACG","String ATTGC is")
DNA_strand("GTAT")  #,"CATA","String GTAT is")    