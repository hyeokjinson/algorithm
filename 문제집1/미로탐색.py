from _collections import deque

dx=[1,0,-1,0]
dy=[0,-1,0,1]

if __name__ == '__main__':
    n,m=map(int,input().split())
    board=[list(map(int,input().strip()))for _ in range(n)]
    dis=[[0]*m for _ in range(n)]
    q=deque()
    q.append((0,0))
    dis[0][0]=1
    while q:
        x,y=q.popleft()

        if x==n-1 and y==m-1:
            break
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<n and 0<=ny<m and board[nx][ny]==1 and dis[nx][ny]==0:
                dis[nx][ny]=dis[x][y]+1
                q.append((nx,ny))

    print(dis[n-1][m-1])
