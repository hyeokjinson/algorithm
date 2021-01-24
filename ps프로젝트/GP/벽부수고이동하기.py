from collections import deque
dx=[1,0,-1,0]
dy=[0,-1,0,1]
def bfs():

    q.append((0,0,0))
    dis[0][0][0]=1

    while q:
        x,y,z=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if arr[nx][ny]==0 and dis[nx][ny][z]==-1:
                    dis[nx][ny][z]=dis[x][y][z]+1
                    q.append((nx,ny,z))
                elif z==0 and arr[nx][ny]==1 and dis[nx][ny][z+1]==-1:
                    dis[nx][ny][z+1]=dis[x][y][z]+1
                    q.append((nx,ny,z+1))

if __name__ == '__main__':
    n,m=map(int,input().split())
    arr=[list(map(int,input().strip()))for _ in range(n)]

    dis=[[[-1]*2 for _ in range(m)] for _ in range(n)]

    q=deque()

    bfs()

    ans1,ans2=dis[n-1][m-1][0],dis[n-1][m-1][1]

    if ans1==-1 and ans2!=-1:
        print(ans2)
    elif ans1!=-1 and ans2==-1:
        print(ans1)
    else:
        print(min(ans1,ans2))
