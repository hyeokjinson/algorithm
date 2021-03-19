if __name__ == '__main__':
    h,w,x,y=map(int,input().split())
    b=[list(map(int,input().split()))for _ in range(h+x)]
    a=[[0 for _ in range(w)]for _ in range(h)]

    for i in range(h+x):
        for j in range(w+y):
            if i<x and j<w:
                a[i][j]=b[i][j]
            elif j<y and i<h:
                a[i][j]=b[i][j]
            elif j>=y and i>=x and j<w and i<h:
                a[i][j]=b[i][j]-a[i-x][j-y]

    for i in range(h):
        for j in range(w):
            print(a[i][j],end=' ')
        print()
