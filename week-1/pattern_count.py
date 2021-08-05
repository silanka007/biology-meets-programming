def pattern_count(pattern, text):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        window = i + len(pattern)
        if text[i:window] == pattern:
            count += 1
    return {"pattern": pattern, "count": count}

  
# print(pattern_count("ACTAT", "ACAACTATGCATACTATCGGGAACTATCCT")) 

