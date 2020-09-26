import copy
from _collections import deque

def bfs():
    global max_
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    check=copy.deepcopy(arr)
    q=deque()
    for i in range(n):
        for j in range(m):
            if arr[i][j]==2:
                q.append((i,j))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if check[nx][ny]==0:
                    check[nx][ny]=2
                    q.append((nx,ny))
    res=0
    for i in range(n):
        for j in range(m):
            if check[i][j] == 0:
                res+=1
    max_=max(max_,res)

def setwall(wall):
    if wall==3:
        bfs()

    else:
        for i in range(n):
            for j in range(m):
                if arr[i][j]==0:
                    arr[i][j]=1
                    setwall(wall+1)
                    arr[i][j]=0



n,m=map(int,input().split())
arr=[list(map(int,input().split()))for _ in range(n)]
max_=-217000000
setwall(0)
print(max_)