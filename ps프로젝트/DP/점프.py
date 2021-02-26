if __name__ == '__main__':
    n=int(input())
    arr=[list(map(int,input().split())) for _ in range(n)]

    dy=[[0]*n for _ in range(n)]
    dy[0][0]=1
    for i in range(n):
        for j in range(n):
            if i==n-1 and j==n-1:
                break

            nx=i+arr[i][j]
            ny=j+arr[i][j]

            if nx<n:
                dy[nx][j]+=dy[i][j]
            if ny<n:
                dy[i][ny]+=dy[i][j]
    print(dy[n-1][n-1])