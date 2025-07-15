### **Task 3 - Comments**

Good comments make your code easier to read, maintain, and share.
They capture ideas that might not be obvious from the code alone and give helpful context to anyone who reads the file later (including future you).

---

#### **Inline comments**

Use the hash symbol `#` to add a short remark at the end of a line or on its own line.

```python
is_admin_user = True   # True means this user is an admin

# Increase the total by one
total_items = total_items + 1
```

Keep inline comments concise and place them near the code they explain.

---

#### **Multiline comments and docstrings**

Triple quotes (`"""`) let you write longer, multi-line explanations.
They are handy for file headers, detailed notes, or function documentation.

```python
"""
This section loads customer data from a CSV file,
cleans the records, and prepares them for analysis.
"""
```

Inside a function, a triple-quoted string becomes that function’s docstring, which tools like `help()` and IDE pop-ups will display.

```python
def add(a, b):
    """
    Return the sum of two numbers.

    Parameters:
    a (int or float) - first addend
    b (int or float) - second addend
    """
    return a + b
```

---

#### **Commenting etiquette**

* Focus on *why* the code exists, not *what* obvious statements do.
* Keep comments up to date when code changes.
* Avoid redundant comments that simply restate the code.
* Use clear, plain language.

Thoughtful comments turn good code into great code.