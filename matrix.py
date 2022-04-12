def Matrix(a,b,c,d):
    try:
        matrix=[]
        for i in range(b):
            matrix.append([])
            for j in range(a):
                matrix[i].append(c)
                c += d
        for i in range(0, b):
            for j in range(0, a):
                print(matrix[i][j], end=' ')
            print("")
    except Exception:
        print("Что-то введено не так")
