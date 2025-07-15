### **Task 8 - Number functions**

Python offers several built-in helpers for numeric work, plus the `math` module for more advanced needs.
See the full catalogue here: [https://docs.python.org/3/library/math.html](https://docs.python.org/3/library/math.html)

---

#### Quick demo

```python
n = -42
print(abs(n))                # absolute value -> 42

print(pow(2, 3))             # exponentiation 2³ -> 8
print(round(3.14159, 2))     # round to 2 decimals -> 3.14

quotient, remainder = divmod(17, 5)
print(quotient, remainder)   # -> 3 2

import math
print(math.sqrt(16))         # square root -> 4.0
print(math.ceil(4.2))        # round up -> 5
print(math.floor(4.8))       # round down -> 4
```

Each call returns a new value.
The original variable stays unchanged unless you assign the result back.

---

#### Your exercise

1. Create a file called `Task_8.py`.
2. Add `num = -15.5`.
3. Print the absolute value of `num`.
4. Print `num` cubed (use `pow(num, 3)` or `num ** 3`).
5. Print `num` rounded to the nearest whole number.
6. `import math` and print both the `ceil` and `floor` of `num`.
7. Use `divmod` to show the quotient and remainder of `100` divided by `7`.

Run the script and check that each result matches what you expect.
