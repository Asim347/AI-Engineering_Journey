# Create a function greet_user(name="Guest").

# Requirements:
# - Display a welcome message.
# - Call it without an argument.
# - Call it with your name.

def greet_user(name="Guest"):
    print(f"Welcome {name}")

greet_user("asim")

def calculate_price(price, quantity=1, discount=0):
    subtotal = price * quantity
    discount_amount = subtotal * (discount / 100)
    final_amount = subtotal - discount_amount
    return final_amount


# Default arguments (quantity=1, discount=0)
print("Default:", calculate_price(25.0))

# Custom quantity, default discount
print("Quantity=3:", calculate_price(25.0, 3))

# Custom quantity and discount
print("Quantity=3, 20% off:", calculate_price(25.0, 3, 20))

# Keyword arguments
print("Keyword discount:", calculate_price(40.0, discount=15))


def create_student(name, course="Python", marks=0, status="Active"):
    return {
        "name": name,
        "course": course,
        "marks": marks,
        "status": status,
    }


# All defaults used except name
print(create_student("Ayesha"))

# Positional override for course and marks
print(create_student("Bilal", "Data Science", 91))

# Keyword overrides for specific fields only
print(create_student("Zainab", marks=84, status="Graduated"))


def shopping_total(prices, tax=0, discount=0):
    if not prices:
        return 0

    subtotal = sum(prices)
    after_discount = subtotal * (1 - discount / 100)
    final_amount = after_discount * (1 + tax / 100)
    return round(final_amount, 2)


# Empty cart check
print("Empty cart:", shopping_total([], tax=10, discount=15))

# Standard cart with default tax and discount
print("Basic cart:", shopping_total([120, 45, 30]))

# Cart with discount and tax
print("Discount + tax:", shopping_total([120, 45, 30], tax=8, discount=10))


# Set default model settings
def generate_response(prompt, temperature=0.7, max_tokens=200):

    # Here we would call an AI model/API
    print(f"Prompt: {prompt}")
    print(f"Temperature: {temperature}")
    print(f"Max tokens: {max_tokens}")

# Use default settings
generate_response("Explain machine learning")

# Customize settings
generate_response("Explain neural networks", temperature=0.3)