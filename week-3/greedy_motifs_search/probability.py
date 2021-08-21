def Pr(text, profile):
    probability = 1

    for pos in range(len(text)):
        nucleotide = text[pos]
        probability *= profile[nucleotide][pos]

    return probability


if __name__ == "__main__":
    """profile = {
        "A": [0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.9, 0.1, 0.1, 0.1, 0.3, 0.0],
        "T": [0.1, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.4, 0.1, 0.2, 0.4, 0.6],
        "G": [0.0, 0.0, 1.0, 1.0, 0.9, 0.9, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0],
        "C": [0.7, 0.2, 0.0, 0.0, 0.1, 0.1, 0.0, 0.5, 0.8, 0.7, 0.3, 0.4],
    }
    print(Pr("ACGGGGATTACC", profile))"""
    prof = {
        "A": [0.4, 0.3, 0.0, 0.1, 0.0, 0.9],
        "C": [0.2, 0.3, 0.0, 0.4, 0.0, 0.1],
        "G": [0.1, 0.3, 1.0, 0.1, 0.5, 0.0],
        "T": [0.3, 0.1, 0.0, 0.4, 0.5, 0.0],
    }
    print(Pr("TCGGTA", prof))
