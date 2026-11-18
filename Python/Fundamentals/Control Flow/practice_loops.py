#1.Print all odd numbers between 1 and 30 using a for loop.

for number in range(1, 30, 2):
    print(number)

#2. Count down from 10 to 1 using while loop

number = 10

while number <= 10:
    print(number)
    number -= 1

number = int(input("Enter a number: "))

result = 1

for num in range(number, 0, -1):
    result = result * num

print("Factorial:", result)
