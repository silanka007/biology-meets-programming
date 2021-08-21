# profile most probable k-mer

# Insert your Pr(text, profile) function here from Motifs.py.

# Write your ProfileMostProbableKmer() function here. The profile matrix assumes that the first row corresponds to A,
# the second corresponds to C, the third corresponds to G, and the fourth corresponds to T. You should represent the
# profile matrix as a dictionary whose keys are 'A', 'C', 'G', and 'T' and whose values are lists of floats

from probability import Pr


def Pr(text, profile):
    probability = 1

    for pos in range(len(text)):
        nucleotide = text[pos]
        probability *= profile[nucleotide][pos]

    return probability


def Count(motifs):
    count = {}  # initializing the count dictionary

    k = len(motifs[0])
    for char in "ATGC":
        # count[char] = [0 for x in range(k)]
        count[char] = []
        for pos in range(k):
            count[char].append(0)

    for row in motifs:
        for pos in range(len(row)):
            char = row[pos]
            count[char][pos] += 1

    return count


def Profile(motifs):
    motifArr = Count(motifs)
    k = len(motifs)

    for nucleo, val in motifArr.items():
        for i in range(len(val)):
            motifArr[nucleo][i] /= k

    return motifArr


def Consensus(motifs):
    motif_arr = Count(motifs)

    consensus_arr = [0 for x in range(len(motifs[0]))]
    consensus_nucleo = ["A" for x in range(len(motifs[0]))]

    for nucleo, val in motif_arr.items():
        for pos in range(len(val)):
            if (val[pos] > consensus_arr[pos]):
                consensus_arr[pos] = val[pos]
                consensus_nucleo[pos] = nucleo

    return "".join(consensus_nucleo)


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
        window = text[i: i + k]
        kmerProb = Pr(window, profile)
        if kmerProb > prob:
            prob = kmerProb
            probableKmer = window

    return probableKmer


def GreedyMotifSearch(Dna, k, t):
    BestMotifs = []
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
    n = len(Dna[0])
    for m in range(n - k + 1):
        Motifs = []
        Motifs.append(Dna[0][m:m + k])
        for j in range(1, t):
            P = Profile(Motifs[0:j])
            Motifs.append(ProfileMostProbableKmer(Dna[j], k, P))
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs


if __name__ == "__main__":
    text = "ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT"
    k = 5
    profile = {
        "A": [0.2, 0.2, 0.3, 0.2, 0.3],
        "C": [0.4, 0.3, 0.1, 0.5, 0.1],
        "G": [0.3, 0.3, 0.5, 0.2, 0.4],
        "T": [0.1, 0.2, 0.1, 0.1, 0.2],
    }
    print(ProfileMostProbableKmer(text, k, profile))
