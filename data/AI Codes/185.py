def main():
    filename = input("Enter filename to write to: ")
    content = input("Enter content to write: ")
    with open(filename, 'w') as file:
        file.write(content)
    print("Content written to", filename)

if __name__ == "__main__":
    main()
