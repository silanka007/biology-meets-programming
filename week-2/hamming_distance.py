# We say that position i in k-mers p and q is a mismatch if the symbols 
# at position i of the two strings are not the same. The total number 
# of mismatches between strings p and q is called the Hamming distance 
# between these strings.

# Hamming Distance Problem: Compute the Hamming distance between two strings.
# Input: Two strings of equal length.
# Output: The Hamming distance between these strings

def hammingDistance(p, q):
    mismatch_count = 0
    maxLen = len(p) if len(p) > len(q) else len(q) 
    
    for i in range(maxLen):
        if p[i] != q[i]:
            mismatch_count += 1
    
    return mismatch_count

if __name__ == "__main__":
    str1 = "AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGCATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCGACTTT"
    str2 = "AGAAACAGACCGCTATGTTCAACGATTTGTTTTATCTCGTCACCGGGATATTGCGGCCACTCATCGGTCAGTTGATTACGCAGGGCGTAAATCGCCAGAATCAGGCTGAAACCCTACGGACAGGTTTACGAACCT"
    hdistance = hammingDistance(str1, str2)
    print(hdistance)