# Create a function called calculate_square().

# Requirements:
# 1. Accept one number.
# 2. Calculate its square.
# 3. Return the result.
# 4. Call it with three different numbers.
# 5. Print all results.

def calculate_square(number):

    result = number*number

    return result

print(calculate_square(4))
print(calculate_square(5))
print(calculate_square(6))

print("------------2-----------")
# Build a bookstore billing function.

# Create calculate_bill(price, quantity).

# Requirements:
# 1. Accept book price and quantity.
# 2. Calculate the total bill.
# 3. Return the total.
# 4. Calculate bills for three different books.
# 5. Print each bill.

def calculate_bill(price, quantity):
    total_bill = price * quantity
    return total_bill

print(calculate_bill(500, 3))
print(calculate_bill(600, 4))
print(calculate_bill(700, 5))



print("------------3-----------")
# Build a student result analyzer.

# Create analyze_result(marks).

# Requirements:
# 1. Accept a list of marks.
# 2. Calculate total marks.
# 3. Calculate average marks.
# 4. Find the highest and lowest marks.
# 5. Return all results.


def analyze_result(marks):
    if not marks:
        return None

    total = 0
    highest = marks[0]
    lowest = marks[0]

    for num in marks:
        total += num
        if num > highest:
            highest = num
        if num < lowest:
            lowest = num

    average = total / len(marks)

    return {
        "total": total,
        "average": average,
        "highest": highest,
        "lowest": lowest,
    }

result = analyze_result([3,4,5,3,2])
print(result['total'])
print(result['average'])
print(result['highest'])
print(result['lowest'])



# Build a number classification function.

# Create analyze_number(number).

# Requirements:
# 1. Identify whether the number is positive, negative or zero.
# 2. Identify whether it is even or odd.
# 3. Return meaningful results.
# 4. Test with at least five different numbers.

def analyze_number(number):
    if number == 0:
        sign = "Zero"
    elif number > 0:
        sign = "Positive"
    else:
        sign = "Negative"

    parity = "Even" if number % 2 == 0 else "Odd"

    return {
        "number": number,
        "sign": sign,
        "parity": parity,
    }


test_numbers = [3, 4, -4, -7, 0]
for num in test_numbers:
    print(analyze_number(num))