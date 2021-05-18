def BruteForceStringMatch(text, pattern):
    n = len (text)
    m = len (pattern)
    for i in range (n-m):
        j = 0
        while j < m and pattern[j] == text[i + j]:
            j += 1
        if j == m:
            return i
    return -1



word = "Anatomy"
file = open("shark.txt", "r")
text = file.read()

print (BruteForceStringMatch(text, word))
