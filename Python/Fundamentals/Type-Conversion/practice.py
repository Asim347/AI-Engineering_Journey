"""
Practice Tasks for Type Conversion:

1. User Input Calculator: 
   Write code where user_epochs = "10" (a string) is converted into an 
   integer, then multiplied by 2 to print a final epoch count message.

2. Precision Loss Test: 
   Create a float variable model_score = 89.95, cast it to an int, 
   and print what happens to the decimal portion.

3. Immutable Cast: 
   Create a list active_users = ["Asim", "Ali", "Sara"] and convert 
   it into a tuple to ensure it cannot be modified accidentally.
"""

# First one (Improved f-string)
user_epochs = "10"
new_user_epoch = int(user_epochs)
multiple_of_two = new_user_epoch * 2
# We wrap 'user_epochs' and 'type(user_epochs)' inside {} so Python evaluates them
print(f"Original value: {user_epochs} (Type: {type(user_epochs)}) | Converted int: {new_user_epoch} | Doubled: {multiple_of_two}")

# 2nd One

model_score = 89.95
converted = int(model_score)
print(converted)

# 3. Immutable Cast
active_users = ["Asim", "Ali", "Sara"]  # This is a list (mutable)

# Convert the list to a tuple using tuple()
immutable_users = tuple(active_users)

print("Converted tuple:", immutable_users)
print("New type:", type(immutable_users))