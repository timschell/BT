def main():
    filename = input("Enter filename to read: ")
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:\n", content)
    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
    main()
