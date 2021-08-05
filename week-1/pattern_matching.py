# Write a function PatternMatching that solves the Pattern Matching Problem.
def pattern_matching(pattern, genome):
    positions = []
    for i in range(len(genome) - len(pattern) + 1):
        window = genome[i: i + len(pattern)]
        if window == pattern:
            positions.append(str(i))

    return " ".join(positions)


print(pattern_matching('ATAT', 'GATATATGCATATACTT'))
