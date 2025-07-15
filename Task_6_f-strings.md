### **Task 6 - Formatted strings (f-strings)**

Formatted strings let you embed variables **and** expressions directly inside a string by prefixing it with `f` (for “formatted”) and wrapping the value you want to insert in curly braces `{ }`.

```python
first_name = "Alice"
age = 30
greeting = f"{first_name} is {age} years old."
print(greeting)           # Alice is 30 years old.
```

Anything inside the braces is evaluated first, then converted to text:

```python
width = 5
height = 3
print(f"Area: {width * height}")   # Area: 15
```

You can mix regular text and multiple placeholders in the same string.

---

#### **Your exercise**

1. Create a file called `Task_5.py`.
2. Inside it, declare three variables: `first_name`, `last_name`, and `age`.
3. Build a string called `intro` that reads:
   `Hi <first_name> <last_name>! You are <age> years old.`
   Use a single f-string, then print `intro`.
4. Add another print that uses an expression inside the braces to show the person’s age **two years from now**. Example output:
   `In two years you will be 27.`

When you run the file you should see two neatly formatted sentences that prove you have mastered basic f-strings.
