# Code Challenge (3 points): Write a function ApproximatePatternMatching 
# to solve the Approximate Pattern Matching Problem. 
# (Make sure to use HammingDistance as a subroutine!)

# Input:  Strings Pattern and Text along with an integer d
# Output: A list containing all starting positions where Pattern appears
# as a substring of Text with at most d mismatches
from hamming_distance import hammingDistance

def ApproximatePatternMatching(text, pattern, d):
    positions = []
    
    for i in range(len(text) - len(pattern) + 1):
        window = text[i:i+len(pattern)]
        hDistance = hammingDistance(pattern, window)
        if hDistance <= d:
            positions.append(i)
    
    return positions


if __name__ == "__main__":
    text = "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT"
    pattern = "ATTCTGGA"
    d = 3
    approxPositions = ApproximatePatternMatching(text, pattern, d)
    print(approxPositions)