### Task 4 - Indexing characters in a string

In Python you can grab a single character from a string with square-bracket notation `[]`.
Counting starts at 0, so the first character is index `0`, the second is `1`, and so on.

```python
reviewer_name = "Alice"
print(reviewer_name[0])   # A
print(reviewer_name[1])   # l
print(reviewer_name[4])   # e
```

> **Hint:** A negative index counts from the end.
> `reviewer_name[-1]` is the last character (`"e"`), `reviewer_name[-2]` is the second-to-last (`"c"`).

#### Your exercise

1. Create a variable called `pet_name` and assign any short word (e.g. `"Buddy"`).
2. Print the first character, the third character, and the last character—each on its own line.

---

### Task 4.1 - Indexing items in a list

The very same brackets work on lists (and most other sequences):

```python
fruit_basket = ["apple", "banana", "cherry", "date"]
print(fruit_basket[0])   # apple
print(fruit_basket[2])   # cherry
print(fruit_basket[-1])  # date
```

> **Hint:** Just like with strings, lists start at index `0`, and negative indices work from the end.

#### Your exercise

1. Make a list named `scores` that holds five numbers of your choice.
2. Print the second score, then the last score, each on its own line.
3. (Extra) Change the middle score (index 2) to `100`, then print the whole list to confirm the change.