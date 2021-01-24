from collections import deque
dx=[1,0,-1,0]
dy=[0,-1,0,1]

def bfs():
    day=-1

    while q:
        day+=1
        qlen=len(q)

        while qlen:
            x,y=q.popleft()

            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]

                if 0<=nx<n and 0<=ny<m:
                    if arr[nx][ny]==0:
                        arr[nx][ny]=arr[x][y]+1
                        q.append((nx,ny))
            qlen-=1

    for i in range(n):
        for j in range(m):
            if arr[i][j]==0:
                return -1
    return day


if __name__ == '__main__':
    m,n=map(int,input().split())
    arr=[list(map(int,input().split()))for _ in range(n)]

    q=deque()
    for i in range(n):
        for j in range(m):
            if arr[i][j]==1:
                q.append((i,j))

    print(bfs())