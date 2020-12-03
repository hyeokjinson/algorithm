from _collections import deque
from copy import deepcopy
import sys

input=sys.stdin.readline

def bfs():
    global res
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    q=deque()
    check=deepcopy(arr)
    for i in range(n):
        for j in range(m):
            if check[i][j]==2:
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
    cnt=0
    for i in range(n):
        for j in range(m):
            if check[i][j]==0:
                cnt+=1
    if res>cnt:
        return
    res=max(res,cnt)

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



if __name__ == '__main__':
    n,m=map(int,input().split())
    arr=[list(map(int,input().split()))for _ in range(n)]

    res=-2147000000

    setwall(0)
    print(res)