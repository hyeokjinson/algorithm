from collections import deque

dx=[1,0,-1,0]
dy=[0,-1,0,1]

if __name__ == '__main__':
    n,m=map(int,input().split())
    arr=[list(map(int,input().strip()))for _ in range(n)]
    ch=[[0]*m for _ in range(n)]
    q=deque()
    q.append((0,0))
    ch[0][0]=1

    while q:
        x,y=q.popleft()
        if x==n-1 and y==m-1:
            print(ch[n-1][m-1])
            break
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<n and 0<=ny<m and arr[nx][ny]==1:
                if ch[nx][ny]==0:
                    ch[nx][ny]=ch[x][y]+1
                    q.append((nx,ny))
