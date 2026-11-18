#Task 1

temperature = 50
if temperature  > 30:
    print("it is hot")

#Task 2

number = 4

if number % 2 ==0:
    print("Even number")
else:
    print("Odd number")


#Task 3

marks = 87

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F")

#Task 4

username = "admin"
password = "python123"

if username == "admin" and password == "python123":
    print("Valid Credintals")
else:
    print("Invalide Credinatls")

#Task 5

units = 50

if units <= 100:
    cost_of_unit = 10
elif units <= 200:
    cost_of_unit = 15
else:
    cost_of_unit = 20

total_bill = units * cost_of_unit

print(f"Total electricity bill: Rs. {total_bill}")