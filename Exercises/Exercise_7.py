"""### Exercise 7: Find the number of occurrences of a substring in a string
Write a Python code to find how often the substring “Emma” appears in the given string.

Given:
str_x = "Kittens are very cute. Kittens like to play."""

def substring_counter(str_x, substring):
   x = str_x.count(substring)
   print(f"{substring} appeared {x} times.")

str_x = input("Given string: ")
substring = input("Word to count: ")

substring_counter(str_x, substring)