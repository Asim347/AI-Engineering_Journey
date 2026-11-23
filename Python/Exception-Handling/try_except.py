try:
    number = int("Hello")

except ValueError:
   print("Enter a valid value")

print("Program contiues...")



try:
    a = int(input("Enter a number"))
    b = int(input("Enter another number"))
    result = a / b
except ValueError:
    print("Enter a valid numbers")


except ZeroDivisionError:
    print("Zero is not divide able")

else:
    print("Result : ", result)

finally:
    print("Operation completed")


try:
    tokens = int(input("Enter token count: "))
    price = float(input("Enter price per 1000 tokens: "))

    if tokens < 0 or price < 0:
        raise ValueError("Tokens and price cannot be negative.")

    cost = (tokens / 1000) * price

except ValueError as err:
    print("Invalid input:", err)

else:
    print("API Cost:", cost)

finally:
    print("Calculation completed.")