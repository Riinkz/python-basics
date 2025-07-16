### **Task 12 - Logical operators**

`and`, `or`, and `not` combine or invert boolean expressions.
Python stops evaluating as soon as the final truth value is known, a behavior called **short-circuiting**.

---

#### Quick demo

```python
has_passport = True
has_visa = False
is_citizen = False

# Both conditions must be true
if has_passport and has_visa:
    print("Border cleared")        # not printed

# At least one condition is true
if has_passport or is_citizen:
    print("Document accepted")     # printed

# Invert a condition
if not is_citizen:
    print("Non-citizen warning")   # printed

age = 30
# Chained comparison reads naturally
if 18 <= age < 65:
    print("Working-age adult")
```

---

#### Your exercise

1. Create a file called `Task_12.py`.

2. Set these variables:

   ```python
   high_income = False
   good_credit = True
   student = True
   ```

3. Write logic that prints **"Eligible for loan"** only when the applicant has `high_income` **and** `good_credit` **and** is **not** a `student`. Otherwise print **"Not eligible"**.

4. Add a second check that prints **"Maybe eligible"** when the applicant has either `high_income` **or** `good_credit`, provided they are **not** a `student`.

5. Finally, define `age` as your age and use a chained comparison to print **"Within target age range"** when `age` is between 18 and 65 inclusive.

Run the script and toggle the boolean variables to see how each logical operator affects the outcome.
