# Write a function SkewArray(Genome) that takes a DNA string Genome as input 
# and returns the skew array of Genome in the form of a list whose i-th 
# element is Skew[i]. Then add this function to Replication.py.
import matplotlib.pyplot as plt

def skewArray(genome):
    array = [0 for i in range(len(genome) + 1)]

    for i in range(len(genome)):
        if genome[i] == 'A' or genome[i] == 'T':
            array[i+1] = array[i]
        elif genome[i] == 'G':
            array[i+1] = array[i] + 1
        elif genome[i] == 'C':
            array[i+1] = array[i] - 1
    return array


def skewArray2(genome):
    array = [0 for i in range(len(genome) + 1)]
    result = {}

    for i in range(len(genome)):
        if genome[i] == 'A' or genome[i] == 'T':
            array[i+1] = array[i]
        elif genome[i] == 'G':
            array[i+1] = array[i] + 1
        elif genome[i] == 'C':
            array[i+1] = array[i] - 1
    for i in range(len(array)):
        result[i] = array[i]
    return result

if __name__ == '__main__':
    array = skewArray('AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGCATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCGACTTT')
    plt.plot(array[:], marker='o')
    plt.show()

