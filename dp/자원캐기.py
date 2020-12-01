if __name__ == '__main__':
    n,m=map(int,input().split())

    arr=[list(map(int,input().split()))for _ in range(n)]
    dy=[[0]*m for _ in range(n)]

    dy[0][0]=arr[0][0]

    for i in range(1,n):
        dy[i][0]=dy[i-1][0]+arr[i][0]

    for i in range(1,m):
        dy[0][i] = dy[0][i - 1] + arr[0][i]

    for i in range(1,n):
        for j in range(1,m):
            dy[i][j]=max(dy[i-1][j],dy[i][j-1])+arr[i]x[j]

    print(dy[n-1][m-1])