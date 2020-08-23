def quad_tree(x,y,n):
    global matrix,blue,white
    color=matrix[y][x]
    double_break=False

    for i in range(x,x+n):
        if double_break:
            break
        for j in range(y,y+n):
            if matrix[j][i]!=color:
                quad_tree(x,y,n//2)
                quad_tree(x+n//2,y,n//2)
                quad_tree(x,y+n//2,n//2)
                quad_tree(x+n//2,y+n//2,n//2)
                double_break=True
                break

    if not double_break:
        if matrix[y][x]==1:
            blue+=1
        else:
            white+=1

n=int(input())
matrix=[list(map(int,input().split()))for _ in range(n)]
blue=0
white=0
quad_tree(0,0,n)
print(white)
print(blue)

