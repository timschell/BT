def count_words_in_file(filename):
    with open(filename, 'r') as file:
        text = file.read()
    words = text.split()
    return len(words)

def main():
    filename = input("Enter the filename: ")
    word_count = count_words_in_file(filename)
    print(f"The file {filename} has {word_count} words.")

if __name__ == "__main__":
    main()
