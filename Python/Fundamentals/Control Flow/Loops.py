#for variable in sequence:
    # code to execute

for number in range(1, 6):
    print(number)

for number in range(2, 11, 2):
    print(number)

#while condition:
    # code to execute

number = 1

while number <= 5:
    print(number)
    number += 1

password = ""

while password != "python123":
    password = input("Enter password: ")

print("Access granted")


for number in range(1, 10):
    if number == 5:
        break

    print(number)


for number in range(1, 6):
    if number == 3:
        continue

    print(number)