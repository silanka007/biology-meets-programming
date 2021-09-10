def Pr(text, profile):
    probability = 1

    for pos in range(len(text)):
        nucleotide = text[pos]
        probability *= profile[nucleotide][pos]

    return probability


def Score(motifs):
    consensus_str = Consensus(motifs)
    score = 0

    for row in motifs:
        for pos in range(len(row)):
            if row[pos] != consensus_str[pos]:
                score += 1

    return score


def ProfileMostProbableKmer(text, k, profile):
    probableKmer = text[0:k]
    prob = 0

    for i in range(len(text) - k + 1):
        window = text[i : i + k]
        kmerProb = Pr(window, profile)
        if kmerProb > prob:
            prob = kmerProb
            probableKmer = window

    return probableKmer


# Code Challenge (2 points): Write a function CountWithPseudocounts(Motifs)
# that takes a list of strings Motifs as input and returns the count
# matrix of Motifs with pseudocounts as a dictionary of lists.
def CountWithPseudocounts(motifs):
    counts = {x: [0 for x in range(len(motifs[0]))] for x in ["A", "C", "G", "T"]}

    for row in motifs:
        for pos in range(len(row)):
            counts[row[pos]][pos] += 1

    for nucleo, val in counts.items():
        for i in range(len(val)):
            val[i] += 1

    return counts


def Consensus(motifs):
    motif_arr = CountWithPseudocounts(motifs)

    consensus_arr = [0 for x in range(len(motifs[0]))]
    consensus_nucleo = ["A" for x in range(len(motifs[0]))]

    for nucleo, val in motif_arr.items():
        for pos in range(len(val)):
            if val[pos] > consensus_arr[pos]:
                consensus_arr[pos] = val[pos]
                consensus_nucleo[pos] = nucleo

    return "".join(consensus_nucleo)


# Code Challenge (3 points): Now that you have written a function
# CountWithPseudocounts(Motifs), write a function
# ProfileWithPseudocounts(Motifs) that takes a list of strings Motifs
# as input and returns the profile matrix of Motifs with pseudocounts
# as a dictionary of lists.
def ProfileWithPseudocounts(motifs):
    # since we added 1 in CountWithPseudocounts, we will add
    # 4 to account for pseudocount (ie the possibility of a nucleo occurring)
    divisor = len(motifs) + 4
    countMotif = CountWithPseudocounts(motifs)

    for nucleo, val in countMotif.items():
        for pos in range(len(val)):
            val[pos] /= divisor

    return countMotif


# Code Challenge (3 points): Write a function
# GreedyMotifSearchWithPseudocounts(Dna, k, t) that takes a list of strings
# Dna followed by integers k and t and returns the result of running
# GreedyMotifSearch, where each profile matrix is generated with pseudocounts.
def GreedyMotifSearchWithPseudocounts(dna, k, t):
    BestMotifs = []
    for i in range(0, t):
        BestMotifs.append(dna[i][0:k])
    n = len(dna[0])

    for m in range(n - k + 1):
        Motifs = []
        Motifs.append(dna[0][m : m + k])
        for j in range(1, t):
            P = ProfileWithPseudocounts(Motifs[0:j])
            Motifs.append(ProfileMostProbableKmer(dna[j], k, P))
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs


# Code Challenge (2 points): Write a function Motifs(Profile, Dna) that takes a 
# profile matrix Profile corresponding to a list of strings Dna as input and 
# returns a list of the Profile-most probable k-mers in each string from Dna.
def Motifs(profile, dna):


if __name__ == "__main__":
    ProfileTestCase0= { 'A': [0.8, 0.0, 0.0, 0.2 ],
    'C': [ 0.0, 0.6, 0.2, 0.0], 
    'G': [ 0.2 ,0.2 ,0.8, 0.0], '
    '         T': [ 0.0, 0.2, 0.0, 0.8]
    }  
    DnaTC0=['TTACCTTAAC','GATGTCTGTC','ACGGCGTTAG','CCCTAACGAG','CGTCAGAGGT']

