num = input("Enter a number: ")

def palindrome_check(num):
    num = str(num)
    if num == num[::-1]:
        print(f"Yes, {num} is a palindrome number!")
    else:
        print(f"No, {num} is not a palindrome number!")
    
palindrome_check(num)