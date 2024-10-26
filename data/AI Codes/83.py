import hashlib

def shorten_url(url):
    hash_object = hashlib.md5(url.encode())
    short_url = hash_object.hexdigest()[:6]
    return f"short.url/{short_url}"

def main():
    print("URL Shortener")
    url = input("Enter URL to shorten: ")
    short_url = shorten_url(url)
    print(f"Shortened URL: {short_url}")

if __name__ == "__main__":
    main()
