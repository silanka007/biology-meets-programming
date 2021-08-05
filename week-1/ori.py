# In the rest of this chapter, we will focus on the relatively easy case of
#  finding ori in bacterial genomes, most of which consist of a single 
# circular chromosome. Research has shown that the region of the bacterial 
# genome encoding ori is typically a few hundred nucleotides long. Our plan
#  is to begin with a bacterium in which ori is known, and then determine
#  what makes this genomic region special in order to design a computational
#  approach for finding ori in other bacteria. Our example is Vibrio cholerae,
#  the pathogenic bacterium that causes cholera; here is the nucleotide
#  sequence appearing in the ori of Vibrio cholerae:


dna = ""
with open("./cholera.txt", "r") as sequence:
  dna = sequence.read()

len_of_cholera_ori = len(dna)

print(len_of_cholera_ori)