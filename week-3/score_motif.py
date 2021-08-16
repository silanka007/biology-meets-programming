from consensus_motif import Consensus


def Score(motifs):
    consensus_str = Consensus(motifs)
    score = 0

    for row in motifs:
        for pos in range(len(row)):
            if row[pos] != consensus_str[pos]:
                score += 1

    return score


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

    print(Score(motifs))
