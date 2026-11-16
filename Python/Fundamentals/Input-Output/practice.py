"""
Practice Tasks for Input/Output:

1. Dynamic Batch Calculator: 
   Ask the user to enter a batch size using input() (e.g., "32"). 
   Since input() returns a string, convert it to an int, multiply it 
   by 4, and print the total dataset slice size.

2. Custom Formatting: 
   Print the words "Model", "Weights", and "Biases" on a single line 
   using print(), but separate them using a pipe character (` | `).
"""
batch_size = int(input("Enter your batch size"))
#converted = int(batch_size)
multiple_of_four = batch_size*4
print(f"{multiple_of_four}")

# 2
print("Model","Weights","Biases", sep='|')