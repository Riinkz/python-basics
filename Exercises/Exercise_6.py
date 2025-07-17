# Either hard code the list or take a user input and split it up in separate ints
# numbers = [10, 20, 33, 46, 55]
raw = input("List of numbers, divided by spaces: ")
numbers = list(map(int, raw.split()))

def div_by_5(numList):
    print("Given list is", numList)
    print("Divisible by 5:")
    for num in numList:
        if num % 5 == 0:
            print(num)
            
div_by_5(numbers)