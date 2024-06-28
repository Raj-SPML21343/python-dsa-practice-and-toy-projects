def rotate(matrix):

    # step1 : find Transpose of a matrix
    N = len(matrix)
    for i in range(N):
        for j in range(i, N):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        print(matrix)
    # step2: change the columns s.t col 0 <-> col N-1, col 1 <-> col N-2, so on..
    for i in range(N):
        for j in range(N//2):
            matrix[i][j], matrix[i][-1-j] = matrix[i][-1-j], matrix[i][j]
    return matrix


print("Question 12: ")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate(matrix)
print(matrix)
