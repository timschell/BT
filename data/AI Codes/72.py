def merge_files(file_list, output_file):
    with open(output_file, 'w') as outfile:
        for file_name in file_list:
            with open(file_name, 'r') as infile:
                outfile.write(infile.read() + "\n")
    print(f"Files merged into {output_file}")

def main():
    file_list = input("Enter file names to merge (comma separated): ").split(", ")
    output_file = input("Enter name of output file: ")
    merge_files(file_list, output_file)

if __name__ == "__main__":
    main()
