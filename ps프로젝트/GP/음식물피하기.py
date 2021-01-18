import sys
sys.setrecursionlimit(100000)
dx=[1,0,-1,0]
dy=[0,-1,0,1]

def dfs(x,y):
    global cnt

    cnt+=1
    visit[x][y]=True

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0<=nx<n and 0<=ny<m and arr[nx][ny]==1:
            if not visit[nx][ny]:
                dfs(nx,ny)
if __name__ == '__main__':
    n,m,k=map(int,input().split())
    arr=[[0]*m for _ in range(n)]
    res=-2147000000
    visit=[[False]*m for _ in range(n)]

    for _ in range(k):
       a,b=map(int,input().split())
       arr[a-1][b-1]=1

    for i in range(n):
        for j in range(m):
            if arr[i][j]==1 and visit[i][j]==False:
                cnt=0
                dfs(i,j)
                res=max(res,cnt)
    print(res)