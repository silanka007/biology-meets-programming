# Input:  A set of kmers Motifs
# Output: Count(Motifs)
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


if __name__ == "__main__":
    motifs = [
        "GTACAACTGT",
        "CAACTATGAA",
        "TCCTACAGGA",
        "AAGCAAGGGT",
        "GCGTACGACC",
        "TCGTCAGCGT",
        "AACAAGGTCA",
        "CTCAGGCGTC",
        "GGATCCAGGT",
        "GGCAAGTACC",
    ]

    print(Count(motifs))
