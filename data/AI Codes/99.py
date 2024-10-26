import csv

def read_csv(file_name):
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def main():
    print("CSV Reader")
    file_name = input("Enter CSV file name: ")
    read_csv(file_name)

if __name__ == "__main__":
    main()
