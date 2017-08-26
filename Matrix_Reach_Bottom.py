def matrix():
    rows=int(input("enter the number of rows: "))
    cols=int(input("enter the number of cols: "))
    array2D=[[x for x in range(0,cols)] for y in range(0,rows)]

    for i in range(cols):
        array2D[0][i]=1
    for i in range(rows):
        array2D[i][0]=1

    for i in range(1,rows):
        for j in range(1,cols):
            array2D[i][j]=array2D[i-1][j]+array2D[i][j-1]+array2D[i-1][j-1]
    for i in range(rows):
        for j in range(cols):
            print(array2D[i][j],end=" ")
        print()
    print(array2D[rows-1][cols-1])
matrix()
