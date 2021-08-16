from count_motif import Count

def Profile(motifs):
    motifArr = Count(motifs)
    k = len(motifs)

    for nucleo, val in motifArr.items():
        for i in range(len(val)):
            motifArr[nucleo][i] /= k

    return motifArr


if __name__ == '__main__':
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

    print(Profile(motifs))