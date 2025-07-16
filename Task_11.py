"""
2. Ask the user for the outside temperature with `input("Temperature in °C: ")`, convert it to `int`, and store it in `temp`.
3. Write an `if-elif-else` chain that prints:

   * `"Hot day"` if `temp` is **30 or above**
   * `"Warm day"` if `temp` is **between 20 and 29**
   * `"Cool day"` otherwise
4. Ask the user for their age, convert it to `int`, and use a **conditional expression** to set `access_msg` to `"You can vote"` or `"You cannot vote yet"`. Print `access_msg`.
5. Run the script with several input combinations to see each branch in action.
"""

# 1. Conditional statements
temperature = input("Temperature in °C: ")

if int(temperature) >= 30:
    print("Hot day")
elif int(temperature) > 19:
    print("Warm day")
else:
    print("Cold day")
    
# 2. Conditional expression
age = input("Age in years: ")

access_msg = "Can vote" if int(age) >= 18 else "Can't vote"
print(access_msg)