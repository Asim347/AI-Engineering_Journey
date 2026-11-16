# 1. Create variables using all eight built-in types
var_int = 42                    # int
var_float = 0.85                # float
var_str = "Transformer"         # str
var_bool = False                # bool
var_list = [10, 20, 30]         # list
var_tuple = (10, 20, 30)        # tuple
var_dict = {"model": "GPT"}     # dict
var_set = {1, 2, 3}             # set

# 2. Check their types using type() and isinstance()
print("\n--- Type Checking ---")
items = [var_int, var_float, var_str, var_bool, var_list, var_tuple, var_dict, var_set]
for item in items:
    print(f"Value: {str(item):<15} | Type: {type(item)}")

# 3 & 4. Modify a list (mutable) vs a tuple (immutable)
print("\n--- Mutability Test ---")
var_list[0] = 99                # Allowed (lists are mutable)
print("Modified list:", var_list)

try:
    var_tuple[0] = 99           # Will raise a TypeError
except TypeError as e:
    print("Tuple error (expected):", e)

# 5. Explore the difference between == and is
print("\n--- Equality (==) vs Identity (is) ---")
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print("a == b (Same values?):", a == b)    # True (Contents match)
print("a is b (Same object in memory?):", a is b)  # False (Different objects)
print("a is c (Same object in memory?):", a is c)  # True (References the exact same object)