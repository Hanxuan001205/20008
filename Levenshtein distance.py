def ld(str1, str2):
    m, n = len(str1)+1,  len(str2)+1
    #初始化矩阵
    matrix = [[0]*n for i in range(m)]
    matrix[0][0] = 0
    for i in range(1, m):
        matrix[i][0] = matrix[i-1][0]+1
    for j in range(1, n):
        matrix[0][j] = matrix[0][j-1]+1
    for i in range(1,m):
        for j in range(1,n):
            if str1[i-1] == str2[j - 1]:
                matrix[i][j] = matrix[i-1][j-1]
            else:
                matrix[i][j] = min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1])+1
    for i in range(0, m):
        print(matrix[i])
    d = matrix[m-1][n-1]
    nd = d/max(len(str1),len(str2))
    sim = 1 - nd
    print("The similarity is: ",sim)
str1 = "ther"
str2 = "ptter"
ld(str1,str2)