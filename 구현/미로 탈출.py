from _collections import deque
dx=[1,0,-1,0]
dy=[0,-1,0,1]
def bfs(x,y):
    dis=[[0]*m for _ in range(n)]
    q=deque()
    q.append((x,y))
    dis[x][y]=1
    while q:
        tmp=q.popleft()
        for i in range(4):
            nx=tmp[0]+dx[i]
            ny=tmp[1]+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if arr[nx][ny]==1:
                    arr[nx][ny]=0
                    dis[nx][ny]=dis[tmp[0]][tmp[1]]+1
                    q.append((nx,ny))
    return dis[n-1][m-1]

n,m=map(int,input().split())
arr=[list(map(int,input().strip()))for _ in range(n)]
print(bfs(0,0))
