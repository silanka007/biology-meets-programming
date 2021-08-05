# finding the reverse complement of DNA string
def reverse_complement(dna_string):
    complement = ""
    reverse_string = ""
    hash_map = {"A": "T", "T": "A", "G": "C", "C": "G"}

    for i in dna_string:
        complement += hash_map[i.upper()]
    for i in range(len(complement) - 1, -1, -1):
        reverse_string += complement[i]
    return reverse_string

reverseStr = reverse_complement("AGTCGCATAGT")
print(reverseStr == "ACTATGCGACT")
print(reverseStr)
