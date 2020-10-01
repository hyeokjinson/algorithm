n=int(input())
m=int(input())
dis=[[2147000000]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    dis[i][i]=0

for _ in range(m):
    a,b,c=map(int,input().split())
    if c<dis[a][b]:
        dis[a][b]=c

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            dis[i][j]=min(dis[i][j],dis[i][k]+dis[k][j])
for i in range(1,n+1):
    for j in range(1,n+1):
        if dis[i][j]==2147000000:
            print(0,end=' ')
        else:
            print(dis[i][j],end=' ')
    print()