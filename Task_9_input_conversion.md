### **Task 9 - User input and type conversion**

The `input()` function pauses your program, shows a prompt, and returns **a string** containing whatever the user typed.
To do arithmetic or other non-text work, convert that string to the needed type.

---

#### Quick demo

```python
x = input("Enter a number: ")   # x is a string
print(type(x))                  # <class 'str'>

# Convert to int, add 1
y = int(x) + 1
print("x + 1 is", y)

# Other built-in converters
int("7")        # -> 7
float("3.14")   # -> 3.14
bool("")        # -> False  (empty string)
bool("hello")   # -> True   (any non-empty string)
str(42)         # -> "42"
```

> **Note:** For booleans, an empty value (`""`, `0`, `0.0`) is `False`.
> Anything else is `True`.

---

#### Your exercise

1. Create a file called `Task_9.py`.
2. Ask the user for their **age** with `input("Age: ")` and store it in `age_str`.
3. Convert `age_str` to an integer named `age_int`.
4. Print a message using an f-string:
   `You will be <age_int + 5> in five years.`
5. Ask the user to enter a decimal **price**, convert it to `float`, add 20% tax, and print the total.
6. Finally, prompt the user for any text, convert it to `bool`, and print whether Python considered it `True` or `False`.

Run the script several times with different inputs to see how each conversion behaves.
