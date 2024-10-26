def count_words(s):
    return len(s.split())

def main():
    s = input("Enter a string: ")
    print("Number of words:", count_words(s))

if __name__ == "__main__":
    main()
