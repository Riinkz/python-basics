"""
2. Ask the user for their **age** with `input("Age: ")` and store it in `age_str`.
3. Convert `age_str` to an integer named `age_int`.
4. Print a message using an f-string:
   `You will be <age_int + 5> in five years.`
5. Ask the user to enter a decimal **price**, convert it to `float`, add 20% tax, and print the total.
6. Finally, prompt the user for any text, convert it to `bool`, and print whether Python considered it `True` or `False`.
"""

# 1. String to integer
age_str = input("Age: ")
age_int = int(age_str)
print(f"You will be {age_int + 5} in five years")

# 2. Tax calculator
price_str = input("Price: ")
price_float = float(price_str)
price_float *= 1.2
print(f"Price after tax: {price_float}")

# 3. Bool
text = input("Text: ")
text_bool = bool(text)
print(text_bool)