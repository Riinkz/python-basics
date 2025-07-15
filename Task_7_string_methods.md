### **Task 7 - String methods**

Python gives every string a toolbox of built-in methods.
You call a method with dot notation, for example `my_text.upper()`.

Below are a few handy ones to get you started.
For the complete reference, see the official list on W3Schools (or similar sites on the web):
[https://www.w3schools.com/python/python_ref_string.asp](https://www.w3schools.com/python/python_ref_string.asp)

---

#### Quick demo

```python
sample = "  Python programming  "

print(sample.strip())          # remove leading and trailing spaces
print(sample.lower())          # all lowercase
print(sample.upper())          # ALL UPPERCASE
print(sample.count("m"))       # how many times 'm' appears
print(sample.replace("Python", "Java"))  # swap words
print(sample.startswith("  P"))          # True or False
print("gram" in sample)        # membership test (True)
```

Each method returns a new string (or a number/boolean) - the original stays unchanged unless you reassign it.

---

#### Your exercise

1. Create a file called `Task_6.py`.
2. Add a variable `quote` and set it to a short sentence of your choice.
3. Use at least four different string methods on `quote`, printing the result of each. Suggestions:

   - `title()`
   - `find()`
   - `replace()`
   - `endswith()`
   - `encode()`

4. After each call, print the original `quote` again to show it has not changed.
5. Finally, print a one-line comment (using `#`) summarizing which method you found most useful.

Run the file and compare your output with the documentation page to see what each method does.
