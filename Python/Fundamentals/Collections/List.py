# A list is an ordered and mutable collection that stores multiple items and allows duplicate values.
# - Ordered: Items maintain their positions.
# - Mutable: You can add, remove, or modify items.
# - Duplicates: Same values can appear multiple times.

fruits = ['Mangos','Apple','Banana','Grapes']
print(fruits)

print(fruits[0])
print(fruits[1])
print(fruits[-1])

#new item
print("New item")
fruits[1] = "Orange" # mdoified
print(fruits)
print(type(fruits))

fruits = ["Apple", "Banana"]

fruits.append("Mango")

print(fruits)

print("Add at a specific location")
fruits = ["Apple", "Mango"]
fruits.insert(1, "Banana")
print(fruits)



fruits = ["Apple", "Banana"]
new_fruits = ["Mango", "Orange"]
fruits.extend(new_fruits)
print(fruits)