# A set is an unordered collection of unique elements that does not allow duplicate values.
# Sets are useful when you need unique values or want to perform mathematical set operations.

numbers = {1, 2, 3, 4, 5}

print(numbers)
print(type(numbers))


numbers = {1, 2, 2, 3, 3, 4, 5}

print(numbers)


numbers = {1, 2, 3}

numbers.add(4)
print(numbers)
numbers.remove(2)

print(numbers)



A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A | B)
print(A & B)
print(A - B)
print(A ^ B)