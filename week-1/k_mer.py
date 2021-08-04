# We use the term k-mer for a string of length k and define 
# PatternCount(Pattern, Text) as the number of times that a k-mer
# Pattern appears as a substring of Text.

# naive approach
def pattern_count(pattern, text):
  return text.count(pattern)

print(pattern_count("at", "at hefdf at dfeffe atded fedat"))


def pattern_count2(pattern, text):
  count = 0
  text_len = len(text)
  pattern_len = len(pattern)
  for i in range(text_len):
    range_num = i + pattern_len
    if(range_num - 1 < text_len):
      check_str = text[i:range_num]
      if(check_str == pattern):
        count += 1
  return count

def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count

print(pattern_count2("ATA", "CGATATATCCATAG"))
print(pattern_count2("at", "at hefdf at dfeffe atded fedat"))