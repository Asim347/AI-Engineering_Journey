# Local	Created inside a function; normally accessible only there.
# Global	Created outside functions; accessible throughout the module.


def process_data():
    # Local variable: belongs to this function
    data = "AI training data"
    print(data)

process_data()
# print(data)  # Error: data is not defined here

# Global variable: defined outside the function
model_name = "GPT"

def show_model():
    print(model_name)  # Access global variable

show_model()

counter = 0
def update_counter():
    global counter  # Allow modification of global variable
    counter += 1
update_counter()
print(counter)  # 1


