# Code Challenge (3 points): Implement the ApproximatePatternCount function in Python.

# Input:  Strings Pattern and Text, and an integer d
# Output: The number of times Pattern appears in Text with at most d mismatches
from hamming_distance import hammingDistance

def ApproximatePatternCount(pattern, text, d):
    count = 0
    
    for i in range(len(text) - len(pattern) + 1):
        window = text[i:i+len(pattern)]
        hDistance = hammingDistance(pattern, window)
        if hDistance <= d:
            count += 1
    return count


if __name__ == "__main__":
    text = "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT"
    pattern = "ATTCTGGA"
    d = 3
    approxPositions = ApproximatePatternCount(pattern, text, d)
    print(approxPositions)
    
    text2 = "AAA"
    pattern2 = "AA"
    d2 = 0
    approxPosition = ApproximatePatternCount(pattern2, text2, d2)
    print(approxPosition)