### **Task 15 - Functions and arguments**

A function groups reusable code.
You define it with `def`, give it a name, and list any **parameters** inside parentheses.

---

#### Demo 1 - Simple function, no parameters

```python
def hello_world():
    print("Hello, World!")

hello_world()     # call the function
```

---

#### Demo 2 - Positional and keyword arguments

```python
def greeting(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")

greeting("John", "Doe")                 # positional
greeting(first_name="Jane", last_name="Doe")   # keyword
```

All required parameters must be supplied, either by position or by name.

---

#### Demo 3 - Returning a value

```python
def get_greeting(name):
    return f"Hi {name}"

message = get_greeting("John")    # store the result
print(message)
```

A function can **perform a task** (print) or **return a value** (for later use).

---

#### Demo 4 - Default and variable arguments

```python
def decrement(number, by=1):      # by has a default
    return number - by

print(decrement(10))              # uses default -> 9
print(decrement(10, by=3))        # override default -> 7

def multiply(*numbers):           # * collects any count of arguments
    total = 1
    for number in numbers:
        total *= number
    return total

print(multiply(1, 2, 3, 4))       # 24
```

* Parameters with `=` get default values.
* A star `*` before a name creates a tuple of all extra positional arguments.

---

#### Your exercise

1. Create a file called `Task_15.py`.
2. Write a function `add(x, y)` that returns the sum of its two arguments.
3. Write a function `power(base, exponent=2)` that returns `base` raised to `exponent`.

   * Call it once with one argument (`power(5)`) and once with two arguments (`power(2, 3)`) and print both results.
4. Write a function `average(*scores)` that returns the arithmetic mean of any number of scores.

   * Call it with three different sets of arguments and print each average.
5. Add a short `print_help()` function that prints a one-line description of how to use the program.

   * At the bottom of the file, call `print_help()` so the description shows whenever someone runs the script.

Run `Task_15.py` and verify that each function behaves as specified.
