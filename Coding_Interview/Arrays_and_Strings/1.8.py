def zero_matrix(mat):
    row = [False]*len(mat)
    column = [False]*len(mat[0])
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if (mat[i][j] == 0):
                row[i] = True
                column[j] = True
    # rows
    for i in range(len(mat)):
        if (row[i]):
            for j in range(len(mat[0])):
                mat[i][j] = 0
    # column
    for i in range(len(mat[0])):
        if (column[i]):
            for j in range(len(mat)):
                mat[j][i] = 0

    for rowes in mat:
        print(' '.join(str(num) for num in rowes))
    return mat


zero_matrix([[6, 4, 9, 2, 2, 1, 2, 3, 4],
             [1, 0, 3, 5, 2, 1, 0, 3, 4],
             [8, 3, 9, 6, 1, 1, 2, 3, 4],
             [3, 7, 4, 0, 6, 1, 2, 0, 4],
             [1, 9, 2, 7, 5, 1, 2, 3, 4]])
