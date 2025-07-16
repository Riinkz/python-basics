print("message")

for number in range(3):             # 0 - 2
    print(number + 1, (number + 1) * ".")

 
for number in range(1, 4):          # 1 - 3 
    print(number, number * ".")
    
for number in range(1, 10, 2):      # 1 - 10 in steps of 2
    print(number, number * ".")

# Breaking loops
successful = True                  # True = One attempt | False = 3 attempts
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Not successful after 3 attempts")         # Else is only executed if the loop is not broken


# Nested loops
for x in range(5):              # Outer loop | For a range of 5
    for y in range(3):          # Inner loop (child) | Do 3 times
        print(f"({x}, {y})")
        
# Iterables
print(type(5))
print(type(range(5)))           # Complex type

for x in "Python":
    print(x)
    
for x in ["apple", "banana", "pear"]:
    print(x)