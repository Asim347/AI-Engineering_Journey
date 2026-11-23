# Create a custom exception
class InvalidTemperatureError(Exception):
    pass


def validate_temperature(temperature):

    # Temperature must be between 0 and 2
    if not 0 <= temperature <= 2:
        raise InvalidTemperatureError("Temperature must be between 0 and 2.")

    return "Temperature is valid."


try:
    print(validate_temperature(2.5))

except InvalidTemperatureError as error:
    print("Error:", error)


class InvalidTokenError(Exception):
    pass


def validate_tokens(tokens):

    # Token count must be positive
    if tokens <= 0:
        raise InvalidTokenError("Token count must be positive.")

    return tokens


try:
    result = validate_tokens(-100)
    print("Valid tokens:", result)

except InvalidTokenError as error:
    print("Validation failed:", error)


class InvalidModelConfig(Exception):
    """Raised when AI model configuration values are invalid."""


def validate_config(model_name, temperature, max_tokens):
    if not model_name or not model_name.strip():
        raise InvalidModelConfig("Model name cannot be empty.")

    if not (0 <= temperature <= 2):
        raise InvalidModelConfig("Temperature must be between 0 and 2.")

    if max_tokens <= 0:
        raise InvalidModelConfig("Max tokens must be greater than zero.")

    return {
        "model_name": model_name.strip(),
        "temperature": temperature,
        "max_tokens": max_tokens,
    }


try:
    config = validate_config("gpt-4o", 0.7, 1024)
    print("Valid configuration:", config)

except InvalidModelConfig as err:
    print("Configuration error:", err)

finally:
    print("Validation check finished.")