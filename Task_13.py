"""
2. Write a loop that prints the numbers 1 through 5, each followed by that many asterisks, like
   `3 ***`.
3. Use a second loop with `range(10, 0, -2)` to print even numbers downward: `10  8  6  4  2`.
4. Prompt the user to enter a secret word. Give them up to **3 tries**.

   - If they guess correctly, print `"Access granted"` and end the loop with `break`.
   - If they fail all three attempts, print `"Access denied"` after the loop using the `else` clause.

5. Make a list named `hobbies` with at least three items. Loop through it and print
   `"I enjoy <hobby>"` for each one.
"""

# 1. Simple loops
for i in range(1, 5):
    print(f"{i} {i * "*"}")
    
for n in range(10, 0, -2):
    print(n)  
   
# 2. Secret
secret = "cat"
print("I am both Schrödinger's uncertain prisoner and the cherished companion of Bastet, reigning over memes and mice alike - what am I?")

for i in range(3):
    guess = input("Answer: ")
    if guess.lower() == secret:
        print("Access granted")
        break
    else:
        print("Try again!")
else: 
    print("Access denied")
    
hobbies = ["Eating cables", "Munching electronics", "Tasting hardware"]

# 3. Hobbies
for hobbies in ["eating cables", "munching electronics", "tasting hardware"]:
    print(f"I like {hobbies}!")
