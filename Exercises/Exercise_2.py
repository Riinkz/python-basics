previous_num = 0

for i in range(10):
    current_num = i
    print(f"Current Number {current_num} Previous Number {previous_num} Sum: {current_num + previous_num}")
    previous_num = current_num
    
