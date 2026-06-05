import random
import string

# Store shortened URLs
url_db = {}

def shorten_url(long_url):
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    url_db[code] = long_url
    return f"https://short.ly/{code}"

def get_original_url(short_url):
    code = short_url.split("/")[-1]
    return url_db.get(code, "URL not found")

# Example usage
short = shorten_url("https://www.example.com/very/long/url")
print("Short URL:", short)

original = get_original_url(short)
print("Original URL:", original)