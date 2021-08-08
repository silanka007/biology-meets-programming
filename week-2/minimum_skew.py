# Code Challenge (3 points): Write a function MinimumSkew taking a DNA 
# string Genome as input and returning all integers i minimizing Skew[i] 
# for Genome. Then add this function to Replication.py. (Hint: make sure 
# to call Skew(Genome) as a subroutine, and keep in mind that Python has 
# a built-in min function in addition to max.)

from skew_array import skewArray
import sys

def minimumSkew(genome):
    positions = []
    skew_arr = skewArray(genome)
    minimum = sys.maxsize
    for num in skew_arr:
        if num < minimum:
            minimum = num
    
    for i in range(len(skew_arr)):
        if skew_arr[i] == minimum:
            positions.append(i)
    
    return positions


if __name__ == '__main__':
    positions = minimumSkew("TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT")
    print(positions)