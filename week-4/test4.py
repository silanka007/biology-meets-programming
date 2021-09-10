import random


def WeightedDie(Probabilities):
    count = 0
    p = random.uniform(0, 1)
    for keys, values in Probabilities.items():
        count = count + values
        if p < count:

            return keys


def Normalize(Probabilities):
    # your code here
    sumOfProbabilities = 0
    newlist = {}
    for i in Probabilities:
        sumOfProbabilities += Probabilities.get(i)
    for i in Probabilities:
        newlist[i] = 0
        for j in Probabilities:
            if i == j:
                newlist[i] += Probabilities[j] / sumOfProbabilities
    return newlist
