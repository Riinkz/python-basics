### Exercise 3: Print characters present at an even index number
Write a Python code to accept a string from the user and display characters present at an even index number.

For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.


Expected Output:

```
Orginal String is  PYnative
Printing only even index chars
P
n
t
v
```

<details> <summary>Hint</summary>

* Use the Python input() function to accept a string from a user.
* Calculate the length of the string using the len() function.
* Next, iterate through the characters of the string using a loop and the range() function.
* Use start = 0, stop = len(s) - 1, and step = 2. The step is 2 because we want only even index numbers.
* In each iteration of the loop, use s[i] to print the character present at the current even index number.
</details>