import os

from dotenv import load_dotenv


def get_config() -> dict:
    """Read settings from .env and return them with the right types.

    Raises ValueError if API_KEY is missing or MAX_RETRIES is not an integer.
    """
    load_dotenv()

    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY is missing")

    debug = os.getenv("DEBUG", "false").lower() == "true"

    max_retries_text = os.getenv("MAX_RETRIES", "3")
    try:
        max_retries = int(max_retries_text)
    except ValueError:
        raise ValueError("MAX_RETRIES must be an integer")

    return {
        "api_key": api_key,
        "debug": debug,
        "max_retries": max_retries,
    }


config = get_config()
print("api_key:", "***")
print("debug:", config["debug"], type(config["debug"]))
print("max_retries:", config["max_retries"], type(config["max_retries"]))