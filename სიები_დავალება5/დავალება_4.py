matrix_1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_2 = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

for row in range(len(matrix_1)):
    for col in range(len(matrix_1[row])):
        sum = matrix_1[row][col] + matrix_2[row][col]
        print(sum)
        


