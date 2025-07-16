### **Task 13 - For loops**

A `for` loop repeats a block of code for every item in a **sequence**.
That sequence can be numbers from `range`, the letters in a string, the elements of a list, and so on.

---

#### Demo 1 - Counting with `range`

`range(start, stop, step)` generates numbers up to but **not including** `stop`.

```python
# Count from 1 up to (but not including) 4
for number in range(1, 4):          # 1 2 3
    print(number, number * ".")     # 1 .   2 ..   3 ...
```

You can add a third argument to set the step size.

```python
# Count from 1 to 9 in steps of 2
for number in range(1, 10, 2):      # 1 3 5 7 9
    print(number)
```

---

#### Demo 2 - Stopping early with `break` and using `else`

`break` ends the loop immediately.
An optional `else` block runs **only if the loop finishes without hitting `break`**.

```python
successful = False

for attempt in range(3):
    print("Attempt", attempt + 1)
    if successful:
        print("Succeeded")
        break
else:                               # runs because break was never reached
    print("All attempts failed")
```

---

#### Demo 3 - Looping over other iterables

Any object that can return its items one at a time is an **iterable**.

```python
# Each character in a string
for char in "Python":
    print(char)

# Each element in a list
for fruit in ["apple", "banana", "pear"]:
    print(f"I like {fruit}")
```

---

#### Your exercise

1. Create a file called `Task_13.py`.
2. Write a loop that prints the numbers 1 through 5, each followed by that many asterisks, like
   `3 ***`.
3. Use a second loop with `range(10, 0, -2)` to print even numbers downward: `10  8  6  4  2`.
4. Prompt the user to enter a secret word. Give them up to **3 tries**.

   - If they guess correctly, print `"Access granted"` and end the loop with `break`.
   - If they fail all three attempts, print `"Access denied"` after the loop using the `else` clause.

5. Make a list named `hobbies` with at least three items. Loop through it and print
   `"I enjoy <hobby>"` for each one.

Run the script, experiment with different inputs, and watch how `range`, `break`, and `else` control the flow of your loops.
