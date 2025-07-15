# 1. Declare some descriptive variables
cable_count     = 5          # number of Ethernet cables
tutorial_rating = 4.20       # score out of 5
reviewer_name   = "John"
is_admin_user   = True       # True means this user is an admin

# 2. Show the original values
print("Original values:")
print("Cables:", cable_count)
print("Rating:", tutorial_rating)
print("Name:", reviewer_name)
print("Admin user:", is_admin_user)

# 3. Change a couple of them
cable_count = cable_count + 3   # bought three more cables
tutorial_rating = 4.50          # updated the rating

# 4. Show the new values
print("\nAfter update:")        # '\n' is used as a line-break before the string.
print("Cables:", cable_count)
print("Rating:", tutorial_rating)

# 5. A multi-line string using triple quotes
detailed_review = """
Python basics are so easy!
Variables can hold numbers, text, or True/False values.
"""

print("\nDetailed review:")
print(detailed_review)
