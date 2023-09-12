# function
def rotate(matrix):
    for i, m in enumerate(matrix):
        for j in range(i, len(matrix[i])):
            c = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = c
    for i, m in enumerate(matrix):
        matrix[i] = m[::-1]
    return matrix

# tests:
print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]))