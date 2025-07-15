# 1. Starting value
num = -15.5

# 2. Absolute value
print("Absolute value:", abs(num))

# 3. num cubed
print("Cubed:", pow(num, 3))  # same as num ** 3

# 4. Rounded to nearest whole number
print("Rounded:", round(num))

# 5. Ceiling and floor
import math
print("Ceiling:", math.ceil(num))
print("Floor:", math.floor(num))

# 6. Quotient and remainder of 100 divided by 7
quotient, remainder = divmod(100, 7)
print("divmod(100, 7):", quotient, remainder)
