from itertools import combinations
from _collections import deque
from copy import deepcopy


dx=[1,0,-1,0]
dy=[0,-1,0,1]

def check(arr):

    for i in range(n):
        for j in range(n):
            if arr[i][j]==0:
                return -1
    return 0

def bfs(start,arr):
    q=deque()
    arr=deepcopy(arr)
    visited=[[0]*(len(arr))for _ in range(len(arr))]

    q.extend(start)
    last_cnt=0
    while q:
        c_x,c_y,cnt=q.popleft()
        visited[c_x][c_y]=1
        for i in range(4):
            nx=c_x+dx[i]
            ny=c_y+dy[i]
            if 0<=nx<len(arr) and 0<=ny<len(arr[0]) and visited[nx][ny]!=1 and arr[nx][ny]!=1:
                visited[nx][ny]=1
                if arr[nx][ny]==0:
                    arr[nx][ny]=2
                    last_cnt=cnt+1
                q.append((nx,ny,cnt+1))

    result=check(arr)

    if result==0:
        return last_cnt
    else:
        return -1

if __name__ == '__main__':
    n,m=map(int,input().split())

    arr=[list(map(int,input().split()))for _ in range(n)]

    start=[]

    for i in range(n):
        for j in range(n):
            if arr[i][j]==2:
                start.append((i,j,0))


    candidate=list(combinations(start,m))
    min_=2147000000

    for tmp in candidate:
        value=bfs(tmp,arr)

        if min_>value and value!=-1:
            min_=value
    if min_==2147000000:
        print(-1)
    else:
        print(min_)

