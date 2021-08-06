import os
import matplotlib.pyplot as plt


def PatternCount(pattern, text):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        window = i + len(pattern)
        if text[i:window] == pattern:
            count += 1
    return count



def SymbolArray(genome, symbol):
    array = {}
    genomeLen = len(genome)
    genomeHalfLen = genomeLen//2
    extendedGenome = genome + genome[0:genomeHalfLen]
    
    for i in range(genomeLen):
        window = extendedGenome[i: i + genomeHalfLen]
        array[i] = PatternCount(symbol, window) 
    return array

def v2(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    for i in range(n):
        array[i] = PatternCount(symbol, ExtendedGenome[i:i+(n//2)])
    return array



def SymbolArrayEfficient(genome, symbol):
    array = {}
    genomeLen = len(genome)
    extendedGenome = genome + genome[0:genomeLen//2]
    windowCount = PatternCount(symbol, extendedGenome[0:genomeLen//2])
    array[0] = windowCount

    for i in range(1, genomeLen):
        initial = i - 1
        end = i + genomeLen//2
        if extendedGenome[initial] == symbol:
          windowCount -= 1
        if extendedGenome[end - 1] == symbol:
          windowCount += 1
        array[i] = windowCount
    return array

# inputData = "AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGCATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCGACTTT"

# symbolArray = SymbolArray(inputData, 'A')
# symbolArray2 = v2(inputData, 'A')

# print(symbolArray)
# print(symbolArray2)

if __name__ == '__main__':
    with open(os.getcwd() + '/week-2/e_coli_genome.txt', 'r') as genome:
        # symbolArray = SymbolArray(genome.read(), 'C')
        symbolArray = SymbolArrayEfficient(genome.read(), 'C')
        plt.plot(*zip(*sorted(symbolArray.items())))
        plt.show()
