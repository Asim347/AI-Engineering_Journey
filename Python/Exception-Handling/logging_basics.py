import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Different logging levels
logging.debug("Checking model configuration")
logging.info("AI model initialized")
logging.warning("High token usage detected")
logging.error("API request failed")
logging.critical("Model service unavailable")



import logging

# Save application logs in a file
logging.basicConfig(
    filename="ai_application.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("AI application started")
logging.warning("Token usage is high")
logging.error("Failed to load dataset")




import logging

logging.basicConfig(
    filename="model_logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def run_model(model_name, tokens_used, init_failed=False):
    logging.info("Starting AI model: %s", model_name)

    if init_failed:
        logging.error("Failed to initialize AI model: %s", model_name)
        return

    logging.info("Model '%s' is active.", model_name)

    if tokens_used > 5000:
        logging.warning(
            "High token usage on '%s': %d tokens (exceeds 5,000).",
            model_name,
            tokens_used,
        )
    else:
        logging.info("Token usage on '%s': %d tokens.", model_name, tokens_used)


# Example runs
run_model("gpt-4o", 1200)
run_model("claude-sonnet", 6400)
run_model("broken-model", 0, init_failed=True)