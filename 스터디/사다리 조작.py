def move():
    for i in range(1,m+1):
        num=i
        for j in range(m):
            if arr[num][j]

n,m,h=map(int,input().split())
arr=[[0]*(n+1) for _ in range(m+1)]
for i in range(h):
    a,b=map(int,input().split())
    arr[a][b]=1
    arr[a][b+1]=1
res=0