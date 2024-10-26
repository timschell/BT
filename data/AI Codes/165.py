import base64

def encode_base64(s):
    return base64.b64encode(s.encode()).decode()

def main():
    s = input("Enter a string: ")
    print(f"Base64 Encoded: {encode_base64(s)}")

if __name__ == "__main__":
    main()
