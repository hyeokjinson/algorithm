if __name__ == '__main__':
    n=int(input())

    dis=[list(map(int,input().split()))for _ in range(n)]

    res=[[0]*i for i in range(1,n+1)]

    res[0][0]=dis[0][0]

    for i in range(1,n):
        for j in range(i+1):
            if j==0:
                res[i][j]=res[i-1][j]+dis[i][j]
            elif 0<j<i:
                res[i][j]=max(res[i-1][j-1]+dis[i][j],res[i-1][j]+dis[i][j])
            else:
                res[i][j]=res[i-1][j-1]+dis[i][j]
    print(max(res[n-1]))