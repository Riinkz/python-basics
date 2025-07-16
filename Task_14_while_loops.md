### **Task 14 - While loops**

A `while` loop keeps running **as long as** its condition stays `True`.
If you forget to change the condition inside the loop, it will run forever.

---

#### Demo 1 - Countdown

```python
number = 10

while number >= 0:          # loop stops when number is -1
    print(number)
    number -= 1             # move toward the stopping point

print("Blast-off!")
```

- The loop prints `10 9 8 … 0`.
- Updating `number` (`number -= 1`) is crucial; otherwise the test `number >= 0` would never become `False`.

---

#### Demo 2 - Echo until the user quits

```python
command = ""

while command.lower() != "quit":
    command = input("> ")
    print("ECHO", command)
```

- `.lower()` lets the user type **quit**, **Quit**, or **QUIT**.
- The loop ends only when the typed word equals `"quit"`.

---

#### Your exercise

1. Create a file called `Task_14.py`.
2. **Part A - Countdown**

   - Ask the user for a starting number with `input("Start countdown at: ")` and convert it to `int`.
   - Use a `while` loop to count down to `0`, printing each number on its own line.
   - After the loop, print `"Launch!"`.

3. **Part B - Password gate**

   - Set `password = "letmein"`.
   - Use a `while` loop that keeps asking `input("Password: ")` until the user enters the correct password **or** types `"quit"`.
   - If the user types the right password, print `"Access granted"` and stop the loop with `break`.
   - If they type `"quit"`, print `"Goodbye"` and stop the loop.
   - For any other input, print `"Incorrect - try again"` and continue looping.

Run the script and test each path: successful login, quitting, and repeated wrong attempts - to see how `while`, `break`, and a changing condition control program flow.
