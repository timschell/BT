def remove_element(lst, element):
    lst.remove(element)
    return lst

def main():
    lst = [int(x) for x in input("Enter list of numbers separated by space: ").split()]
    element = int(input("Enter element to remove: "))
    print("List after removal:", remove_element(lst, element))

if __name__ == "__main__":
    main()
