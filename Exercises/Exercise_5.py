def check_first_last(numberList):
    print(f"Given list: {numberList}")
    first_num = numberList[0]
    last_num = numberList[-1]
    if first_num == last_num:
        return True
    else:
        return False


numbers_x = [10, 20, 30, 40, 10]
print(check_first_last(numbers_x))

numbers_y = [75, 65, 35, 75, 30]
print(check_first_last(numbers_y))