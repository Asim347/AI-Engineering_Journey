# A tuple is an ordered and immutable collection that stores multiple items and allows duplicate values.
# The main difference between lists and tuples is that tuples cannot be modified after creation.

colors = ("Red", "Green", "Blue")

print(colors)
print(type(colors))

# accessing tuples
colors = ("Red", "Green", "Blue")

print(colors[0])
print(colors[-1])

number = (10,)
print(number)
print(type(number))

numbers = (10, 20, 30, 20, 40)

print(numbers.count(20))
print(numbers.index(30))