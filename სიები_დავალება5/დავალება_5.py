matrix_1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transpose_matrix = []

for row in range(len(matrix_1)):
    transpose_row = []
    for col in range(len(matrix_1[row])):
        transpose_row.append(matrix_1[col][row])
    transpose_matrix.append(transpose_row)


for row in transpose_matrix:
    print(row)
