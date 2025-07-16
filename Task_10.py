# 1. Simple Comparison
x = 4
y = 9

print(x == y) # False
print(x != y) # True
print(x < y)  # True
print(x >= y) # False

# 2. String comparison
word1 = "Alpha"
word2 = "alpha"

print(word1 == word2) # False
print(word1 < word2)  # True
print(word1 > word2)  # False

# 3. Unicode points
print(ord(word1[0])) # 65
print(ord(word2[0])) # 97

# 4. Comparison with maths
print(x * 2 == y - 1) # True