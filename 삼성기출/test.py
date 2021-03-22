from collections import deque
from copy import deepcopy

def result_check(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j]==0:
                return -1
    return 0

def bfs(start):
    arr=deepcopy(maps)
    dx=[1,0,-1,0]
    dy=[0,-1,0,1]
    q=deque()
    q.extend(start)
    visited=[[0 for _ in range(n)]for _ in range(n)]
    last_cnt=0

    while q:
        x,y,cnt=q.popleft()
        visited[x][y]=1
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<n and 0<=ny<n and arr[nx][ny]!=1 and visited[nx][ny]!=1:
                visited[nx][ny]=1
                if arr[nx][ny]==0:
                    arr[nx][ny]=2
                    last_cnt=cnt+1
                q.append((nx,ny,cnt+1))
    if result_check(arr)==0:
        return last_cnt
    else:
        return -1






def combination(L,s):
    global min_
    if L==m:
        res=[]
        for i in cb:
            res.append(start[i])
        result=bfs(res)
        if min_>=result and result!=-1:
            min_=result
    else:
        for i in range(s,len(start)):
            cb[L]=i
            combination(L+1,i+1)


if __name__ == '__main__':
    n,m=map(int,input().split())
    maps=[list(map(int,input().split()))for _ in range(n)]
    start=[]
    cb=[0]*m
    min_=2147000000

    for i in range(n):
        for j in range(n):
            if maps[i][j]==2:
                start.append((i,j,0))

    combination(0,0)

    if min_==2147000000:
        print(-1)
    else:
        print(min_)

