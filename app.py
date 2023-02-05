from fastapi import FastAPI
import string
import random

app = FastAPI()

# Dictionary to store the URLs
url_map = {}

# Function to generate the short URL key
def generate_key():
    key = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    if key in url_map.values():
        return generate_key()
    return key

@app.post("/shorten_url")
async def shorten_url(url: str):
    if url in url_map:
        return {"short_url": url_map[url]}
    key = generate_key()
    url_map[url] = key
    return {"short_url": key}
