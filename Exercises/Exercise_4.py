word = input("Choose a word: ")
n = int(input("Number of letters to remove: "))

def remove_chars(word, n):
    shortened_word = word[n:]
    return shortened_word

print("Removing characters from a string")
print(remove_chars(word, n)) 
