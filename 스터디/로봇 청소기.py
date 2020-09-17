dx=[-1,0,1,0]
dy=[0,1,0,-1]
def dfs(x,y,d):
    global cnt
    while True:

        for i in range(4):
            res=False
            dd=(d+3)%4
            nx=x+dx[dd]
            ny=y+dy[dd]
            d=dd
            if mat[nx][ny]==0:
                cnt += 1
                mat[nx][ny]=3
                res=True
                x,y=nx,ny
                break
        if not res:
            if mat[x-dx[d]][y-dy[d]]==1:
                return cnt
            else:
                x,y=x-dx[d],y-dy[d]

n,m=map(int,input().split())
r,c,d=map(int,input().split())
mat=[list(map(int,input().split()))for _ in range(n)]
cnt=1
mat[r][c]=3
dfs(r,c,d)
print(cnt)