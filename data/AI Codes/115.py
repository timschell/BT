import qrcode

def generate_qr_code(data, file_name):
    img = qrcode.make(data)
    img.save(file_name)

def main():
    print("QR Code Generator")
    data = input("Enter data to encode: ")
    file_name = input("Enter file name to save QR code (with .png extension): ")
    generate_qr_code(data, file_name)
    print(f"QR code saved as {file_name}")

if __name__ == "__main__":
    main()
