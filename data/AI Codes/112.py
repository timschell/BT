def reverse_file_content(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
    with open(file_name, 'w') as file:
        file.write(content[::-1])

def main():
    print("Text File Reverser")
    file_name = input("Enter file name: ")
    reverse_file_content(file_name)
    print(f"Content of {file_name} has been reversed.")

if __name__ == "__main__":
    main()
