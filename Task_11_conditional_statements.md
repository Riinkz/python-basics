### **Task 11 - Conditional statements**

`if`, `elif`, and `else` let your program choose different paths based on conditions.
Python decides which block to run by testing each expression in order.

---

#### Quick demo

```python
score = 87

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "D"

print(f"Score {score} earns grade {grade}")
```

- Only **one** branch runs.
- Blocks are defined by indentation (four spaces is standard).

A shorter “one-liner” form is called a **conditional expression**:

```python
is_premium_member = True
discount_rate = 0.20 if is_premium_member else 0.05
print(f"Discount: {discount_rate * 100}%")
```

The expression before `if` is the result when the condition is `True`; after `else` is the result when it is `False`.

---

#### Your exercise

1. Create a file called `Task_11.py`.
2. Ask the user for the outside temperature with `input("Temperature in °C: ")`, convert it to `int`, and store it in `temp`.
3. Write an `if-elif-else` chain that prints:

   - `"Hot day"` if `temp` is **30 or above**
   - `"Warm day"` if `temp` is **between 20 and 29**
   - `"Cool day"` otherwise

4. Ask the user for their age, convert it to `int`, and use a **conditional expression** to set `access_msg` to `"You can vote"` or `"You cannot vote yet"`. Print `access_msg`.
5. Run the script with several input combinations to see each branch in action.

Good indentation and clear conditions make your code easy to read and maintain.
