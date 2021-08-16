from count_motif import Count


def Consensus(motifs):
    motif_arr = Count(motifs)

    consensus_arr = [0 for x in range(len(motifs[0]))]
    consensus_nucleo = ["A" for x in range(len(motifs[0]))]

    for nucleo, val in motif_arr.items():
        for pos in range(len(val)):
            if(val[pos] > consensus_arr[pos]):
                consensus_arr[pos] = val[pos]
                consensus_nucleo[pos] = nucleo

    return "".join(consensus_nucleo)


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

    print(Consensus(motifs))
