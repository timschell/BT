def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def main():
    print("Matrix Transpose")
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i+1} elements separated by space: ").split()))
        matrix.append(row)
    transposed = transpose_matrix(matrix)
    print("Transposed Matrix:")
    for row in transposed:
        print(row)

if __name__ == "__main__":
    main()
