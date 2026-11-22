# Create a function that processes an AI prompt using a local variable called prompt. Print the prompt inside the function.

def prompting():
    prompt = "Ai Engineering"
    print(prompt)

prompting()


#2.Create a global variable model_name = "GPT".

# Create two functions:
# - One displays the model name.
# - Another displays a local variable containing the model's temperature.

model_name = "GPT"
def model():
    print(model_name)

def temperature():
    temperature_model  = 0.4
    print("Temperature of a ",model_name, "is ",temperature_model)

model()
temperature()


# Create a global variable request_count = 0.

# Build a function track_request() that:
# - Increments the counter.
# - Returns its updated value.
# - Call it five times.

request_count = 0
def track_request():
    global request_count
    result = request_count = request_count + 1

    return result

print(track_request())
print(track_request())
print(track_request())
print(track_request())
print(track_request())