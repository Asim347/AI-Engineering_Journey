import re
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)

def clean_text(text):

    try:
        # Validate input type
        if not isinstance(text, str):
            raise TypeError("Input must be a string")

        # Reject empty text
        if not text.strip():
            raise ValueError("Text cannot be empty")

        # Convert text to lowercase
        text = text.lower()

        # Remove URLs
        text = re.sub(r'https?://\S+', '', text)

        # Remove special characters
        text = re.sub(r'[^a-z0-9\s]', '', text)

        # Remove extra spaces
        text = re.sub(r'\s+', ' ', text).strip()

        logging.info("Text cleaned successfully")

        return text

    except (TypeError, ValueError) as error:
        logging.error("Cleaning failed: %s", error)
        raise


# Test the cleaner
result = clean_text("HELLO!!! Visit https://example.com")
print(result)