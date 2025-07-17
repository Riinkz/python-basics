### Exercise 4: Remove first n characters from a string

Write a Python code to remove characters from a string from 0 to n and return a new string.

Given:

```python
def remove_chars(word, n):
    # write your code

print("Removing characters from a string")
print(remove_chars("Bonki", 4))
# output 'i' first four characters are removed

print(remove_chars("Bonki", 2))
# output 'nki'
```

Note: n must be less than the length of the string.

<details> <summary>Hint</summary>

Use string slicing to get a substring. Think about how you can use the slicing notation `[:]` along with the value of n to select the portion of the string after the first n characters.

</details>
