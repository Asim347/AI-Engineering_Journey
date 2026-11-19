# Set "Guest" as the default name
def greet(name="Guest"):
    print(f"Hello, {name}!")

# Uses the default value
greet()

# Overrides the default value
greet("Asim")



# Set default values for price and quantity
def calculate_bill(price, quantity=1):

    # Multiply price by quantity
    total = price * quantity

    return total

print(calculate_bill(500))       # Quantity defaults to 1
print(calculate_bill(500, 3))    # Quantity is 3




def student_info(name, age=20, course="Python"):

    # Display student information
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Course: {course}")

student_info("Asim")
student_info("Ali", age=22)
student_info("Sara", 21, "Machine Learning")