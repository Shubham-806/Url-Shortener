import pyshorteners

s = pyshorteners.Shortener()

long_url = input("Enter the long URL to shorten: ")

short_url = s.tinyurl.short(long_url)

print(f"Shortened URL: {short_url}")
    