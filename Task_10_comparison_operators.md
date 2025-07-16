### **Task 10 - Comparison operators**

Comparison operators let you ask questions about values.
They return either `True` or `False`.

| Operator | Meaning               | Example result     |
| -------- | --------------------- | ------------------ |
| `<`      | less than             | `6 < 2`  ➜ `False` |
| `<=`     | less than or equal    | `6 <= 6` ➜ `True`  |
| `>`      | greater than          | `6 > 2`  ➜ `True`  |
| `>=`     | greater than or equal | `6 >= 8` ➜ `False` |
| `==`     | equal                 | `6 == 6` ➜ `True`  |
| `!=`     | not equal             | `6 != 6` ➜ `False` |

Strings compare by Unicode code points, letter by letter:

```python
print("Cello" > "Brass")   # True  because "C" (67) > "B" (66)
print("Cello" == "cello")  # False uppercase C ≠ lowercase c
```

Check code points with `ord()`:

```python
print(ord("a"))  # 97
print(ord("A"))  # 65
```

---

#### Quick demo

```python
a = 10
b = 7
print(a > b)          # True
print(a == "10")      # False (different types)
print("cat" < "dog")  # True
print("10" > "2")     # False ("1" comes before "2")
```

---

#### Your exercise

1. Create a file called `Task_10.py`.
2. Set `x = 4` and `y = 9`.
3. Print the results of these comparisons on separate lines:

   * `x == y`
   * `x != y`
   * `x < y`
   * `x >= y`
4. Define `word1 = "Alpha"` and `word2 = "alpha"`. Compare them with `==`, `<`, and `>`, printing each result.
5. Use `ord()` to print the Unicode code point of the first character in both `word1` and `word2`.
6. Add one line that shows whether `x * 2` is equal to `y - 1`.

Run the script and verify the printed booleans match your expectations.
