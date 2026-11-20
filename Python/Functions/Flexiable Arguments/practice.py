# 1. 
# Create sum_numbers(*args) that accepts any number of numbers and returns their sum.
def sum_number(*args):
    total = sum(args)
    return total

print(sum_number(10,20,30))

# Create book_details(**kwargs) that accepts book information (title, author, price, category) and prints each detail.
def book_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")


book_details(title="AI Engineering", author = "Chip Huyen", Price= 1200, category="AI")


# Create calculate_statistics(*args) that:
# - Finds the sum.
# - Calculates the average.
# - Finds the maximum and minimum.
# - Returns the results in a dictionary.
# Handle the case when no numbers are provided.

def calculate_statistics(*args):
    if not args:
        return None

    total = sum(args)
    average = total / len(args)
    maximum = args[0]
    minimum = args[0]

    for num in args:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num

    return {
        "sum": total,
        "average": average,
        "max": maximum,
        "min": minimum,
    }


print(calculate_statistics(10, 20, 30, 40))
print(calculate_statistics())


def register_student(*subjects, **details):
    for sub in subjects:
        print("Courses to be registered",sub)

    for key, value in details.items():
        print(f"{key} : {value}")

register_student(
    "Python", "Machine Learning", "SQL",
    name="Asim",
    semester=5,
    university="ABC"
)