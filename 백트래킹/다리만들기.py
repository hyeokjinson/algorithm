from collections import deque

dx=[1,0,-1,0]
dy=[0,1,0,-1]

def bfs1(x,y,cnt):

    q.append((x,y))
    c[x][y]=cnt
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<n and 0<=ny<n:
                if arr[nx][ny]==1 and c[nx][ny]==0:
                    c[nx][ny]=cnt
                    q.append((nx,ny))

def bfs(num):
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<n and 0<=ny<n:
                if arr[nx][ny]==1 and c[nx][ny]!=num:
                    return c2[x][y]-1
                if arr[nx][ny]==0 and c2[nx][ny]==0:
                    c2[nx][ny]=c2[x][y]+1
                    q.append((nx,ny))

if __name__ == '__main__':
    n=int(input())
    arr=[list(map(int,input().split())) for _ in range(n)]
    c=[[0]*n for _ in range(n)]
    q,q1=deque(),deque()
    cnt=1

    for i in range(n):
        for j in range(n):
            if arr[i][j]==1 and c[i][j]==0:
                bfs1(i,j,cnt)
                cnt+=1


    result=2147000000

    for k in range(1,cnt):
        q=deque()
        c2=[[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if arr[i][j]==1 and c[i][j]==k:
                    q.append((i,j))
                    c2[i][j]=1

        res=bfs(k)
        result=min(result,res)
    print(result)