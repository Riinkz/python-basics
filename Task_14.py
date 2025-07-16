# Part A - Countdown
start_number = int(input("Start countdown at: "))
while start_number >= 0:
    print(start_number)
    start_number -= 1
else:
    print("Launch!")
    
# Part B - Password gate
password = "letmein"
while True:
    command = input("Password: ")
    if command == password:
        print("Access granted")
        break
    elif command.lower() == "quit":
        print("Goodbye")
        break
    else:
        print("Incorrect - try again")