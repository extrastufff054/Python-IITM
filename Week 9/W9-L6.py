# f = open('test.txt', 'w')
# for i in range(10):
#     f.write(str(i))
# f.close()

# # f = open('test.txt','r')
# # print(f.read())
# # f.close()

# f = open('test.txt','r')

# s = f.seek(4)   # seek() returns the position of the cursor
# print(s,'\n')
# print("---"*20)
# print(f.read(3))    # read() reads the next n characters from the cursor position

# f.close()

f = open('human.txt','r')
f.close()


# Knuth Morris Pratt Algorithm :- To find a substring in a string
def build_partial_match_table(pattern):
    length = len(pattern)
    lps = [0] * length  # Initialize the partial match table with zeros
    j = 0  # Length of the previous longest prefix suffix
    
    for i in range(1, length):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]
        
        if pattern[i] == pattern[j]:
            j += 1
        lps[i] = j
    
    return lps

def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = build_partial_match_table(pattern)
    j = 0  # Index for pattern
    positions = []  # List to store the starting indices of pattern occurrences

    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = lps[j - 1]

        if text[i] == pattern[j]:
            j += 1
            if j == m:
                positions.append(i - m + 1)
                j = lps[j - 1]

    return positions

# Load text and pattern from files
with open("human.txt", "r") as f:
    text = f.read()

with open("pattern_file.txt", "r") as f:
    pattern = f.read()

# Search for the pattern in the text and print the results
positions = kmp_search(text, pattern)
if positions:
    print("Pattern found at indices:", positions)
else:
    print("Pattern not found in the text.")
