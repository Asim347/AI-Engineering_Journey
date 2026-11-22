# The random module generates pseudo-random numbers and selects random elements.

# Common functions:
# Function	Purpose
# random()	Random decimal between 0 and 1
# randint(a, b)	Random integer between a and b, inclusive
# choice()	Select one random item
# sample()	Select unique items without replacement
# shuffle()	Shuffle a list in place

import random

algorithms = ['svm','decision trees','random forest','linear regression']
selected = random.choice(algorithms)
print(selected)



import random

# Dataset containing ten samples
dataset = list(range(1, 11))

# Select three unique samples
selected_samples = random.sample(dataset, 3)

print(selected_samples)


#task 3

training_data = list(range(1,101))
random.seed(42)
sample_data = random.sample(training_data,10)
print(sample_data)