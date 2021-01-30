if __name__ == '__main__':
    n=int(input())
    m=int(input())
    dy=[[0]*(n+1) for _ in range(n+1)]

    for _ in range(m):
        a,b=map(int,input().split())
        dy[a][b]=1

    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if dy[i][k]==1 and dy[k][j]==1:
                    dy[i][j]=1

    for i in range(1,n+1):
        res=0
        for j in range(1,n+1):
            if not dy[i][j] and not dy[j][i]:
                res+=1
        print(res-1)