# A first attempt might look something like this:
word = input("Choose a word: ")
for i in word:
    if word.index(i) % 2 == 0:
        print(i)
# But that doesn't work, since str.index() always returns the position of the first time that character appears in the whole string, not the position of the particular character you’re looping over.

# A better approach is to use the enumerate() function, which returns a tuple containing a count.
for position, character in enumerate(word):
    if position % 2 == 0:
        print(character)

"""       
# Just as a bonus exercise, doing the same with a function
def even_index_print(word):
    for position, character in enumerate(word):
        if position % 2 == 0:
            print(character)
            
even_index_print(input("Choose a word: "))
"""