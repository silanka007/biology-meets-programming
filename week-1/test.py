def pattern_count(pattern, text):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        window = i + len(pattern)
        if text[i:window] == pattern:
            count += 1
    return {"pattern": pattern, "count": count}

  
# print(pattern_count("ACTAT", "ACAACTATGCATACTATCGGGAACTATCCT")) 

def frequencyMap(k_mer, text):
    freqMap = {}
    for i in range((len(text) - k_mer) + 1):
        sub = text[i: i + k_mer]
        if sub in freqMap:
            freqMap[sub] += 1
        else:
            freqMap[sub] = 1
    return freqMap

print(frequencyMap(3 , "CGATATATCCATAG"))

