def rotate_matrix(mat):
    for i in range(len(mat)//2):
        start = i
        end = len(mat) - i - 1
        for j in range(start, end):
            temp = mat[start + j][start]
            mat[start+j][start] = mat[end][start+j]
            mat[end][start+j] = mat[end-j][end]
            mat[end-j][end] = mat[start][end-j]
            mat[start][end-j] = temp
    for row in mat:
        print(' '.join(str(num) for num in row))
    return mat


rotate_matrix([[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]])

rotate_matrix([[6, 4, 9, 2, 5],
               [1, 7, 3, 5, 2],
               [8, 3, 9, 6, 1],
               [3, 7, 4, 8, 6],
               [1, 9, 2, 7, 5]])
