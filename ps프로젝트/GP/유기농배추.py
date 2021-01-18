from collections import deque
dx=[1,0,-1,0]
dy=[0,-1,0,1]
def bfs(x,y):
    q=deque()
    q.append((x,y))
    visit[x][y]=True

    while q:
        c_x,c_y=q.popleft()

        for i in range(4):
            nx=c_x+dx[i]
            ny=c_y+dy[i]
            if 0<=nx<n and 0<=ny<m and arr[nx][ny]==1:
                if not visit[nx][ny]:
                    visit[nx][ny]=True
                    q.append((nx,ny))

if __name__ == '__main__':
    t=int(input())

    for _ in range(t):
        m,n,k=map(int,input().split())
        arr=[[0]*m for _ in range(n)]
        visit=[[False]*m for _ in range(n)]

        for _ in range(k):
            i,j=map(int,input().split())
            arr[j][i]=1

        cnt=0
        for i in range(n):
            for j in range(m):
                if arr[i][j]==1 and visit[i][j]==False:
                    cnt+=1
                    bfs(i,j)
        print(cnt)