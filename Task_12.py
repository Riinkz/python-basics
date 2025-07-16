# 1. Loan check
high_income = False
good_credit = True
student = False

if high_income and good_credit and not student:
    print("Eligible for loan")
elif high_income or good_credit and not student:
    print("Maybe eligible")
else:
    print("Not eligible")
    
# 2. Age check
age = 23
if 18 <= age <= 65:
    print("Within target age range")  