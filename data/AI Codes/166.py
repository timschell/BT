import base64

def decode_base64(s):
    return base64.b64decode(s.encode()).decode()

def main():
    s = input("Enter a Base64 encoded string: ")
    print(f"Decoded: {decode_base64(s)}")

if __name__ == "__main__":
    main()
