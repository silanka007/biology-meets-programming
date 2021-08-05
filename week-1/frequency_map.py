def frequencyMap(k_mer, text):
    freqMap = {}
    for i in range((len(text) - k_mer) + 1):
        sub = text[i: i + k_mer]
        if sub in freqMap:
            freqMap[sub] += 1
        else:
            freqMap[sub] = 1
    return freqMap

print(frequencyMap(3 , "CGCCTAAATAGCCTCGCGGAGCCTTATGTCATACTCGTCCT"))