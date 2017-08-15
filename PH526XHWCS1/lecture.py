def read_seq(filename):
    """ Reads a sequence of characters from a text file and removes special characters
    :param filename: Name of input file
    :return: String read from file with special characters removed
    """
    with open(filename, "r") as f:
        seq = f.read()
        seq = seq.replace("\n", "")
        seq = seq.replace("\r", "")
        return seq


def translate(dna):
    exec(open("./table.py").read())
    protein = ""
    if len(dna) % 3 == 0:
        for i in range(0, len(dna), 3):
            codon = dna[i:i + 3]
            protein += table[codon]
    return protein


prt = read_seq("protein.txt")
dna = read_seq("dna.txt")
dna = dna[20:938]
prt_translated = translate(dna)
prt_translated = prt_translated.replace("_", "")
prt == prt_translated
