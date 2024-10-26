import os

def rename_file(old_name, new_name):
    if os.path.isfile(old_name):
        os.rename(old_name, new_name)
        print(f"File renamed to {new_name}")
    else:
        print("File does not exist.")

def main():
    print("File Renamer")
    old_name = input("Enter current file name: ")
    new_name = input("Enter new file name: ")
    rename_file(old_name, new_name)

if __name__ == "__main__":
    main()
