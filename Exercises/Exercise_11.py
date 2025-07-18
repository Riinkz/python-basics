def number_reverse(number):
    while number > 0:
        last_num = number % 10          # e.g. 7356 / 10 = 735,6 ← Modulo = 6; saving 6 as a number
        number = number // 10           # e.g. 7356 // 10 = 735 ← Removing the last number
        print(last_num, end=" ")
    
number = 7536
number_reverse(number)