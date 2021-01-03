from collections import deque
import copy

def count(arr):
    c_arr=copy.deepcopy(arr)

    for i in range(n):
        for j in range(m):
            cnt=0
            if arr[i][j]>0:
                for k in range(4):
                    nx=i+dx[k]
                    ny=j+dy[k]
                    if 0<=nx<n and 0<=ny<m:
                        if arr[nx][ny]==0:
                            cnt+=1
                if arr[i][j]-cnt<=0:
                    c_arr[i][j]=0
                else:
                    c_arr[i][j]=arr[i][j]-cnt
    return c_arr

def bfs(x,y):
    q=deque()
    q.append((x,y))
    ch[x][y]=0

    while q:
        x,y=q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<n and 0<=ny<m:
                if ch[nx][ny]==-1 and change_arr[nx][ny]!=0:
                    ch[nx][ny]=0
                    q.append((nx,ny))


n,m=map(int,input().split())
maps=[list(map(int,input().split())) for _ in range(n)]
dx=[1,0,-1,0]
dy=[0,-1,0,1]

result=0
while True:
    result+=1
    cnt=0
    ch=[[-1]*m for _ in range(n)]

    change_arr=count(maps)

    for i in range(n):
        for j in range(m):
            if change_arr[i][j]>0 and ch[i][j]==-1:
                bfs(i,j)
                cnt+=1
    maps=copy.deepcopy(change_arr)

    if cnt>=2:
        print(result)
        break
    elif cnt==0:
        print(0)
        break
