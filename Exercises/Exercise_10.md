### Exercise 10: Merge two lists

Given two lists of numbers, write Python code to create a new list containing odd numbers from the first list and even numbers from the second list.

Given:

`list1 = [10, 20, 25, 30, 35]`

`list2 = [40, 45, 60, 75, 90]`

Expected Output:

```
result list: [25, 35, 40, 60, 90]
```

<details> <summary>Hint</summary>

- Create an empty list to store the result.
- Iterate through the first list using a for loop; if a number is odd (check using num % 2 != 0 formula), append it to the new list.
- Next, iterate through the second list; if a number is even (remainder when divided by 2 is 0), append it to the new list. Finally, return the newly created list.
</details>
