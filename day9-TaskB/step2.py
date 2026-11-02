import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("API_KEY")
debug = os.getenv("DEBUG")
max_retries = os.getenv("MAX_RETRIES")

print(api_key)
print(type(api_key))
print(debug)
print(type(debug))
print(max_retries)
print(type(max_retries))

max_retries=int(max_retries)
print(max_retries+1)