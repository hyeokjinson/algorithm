from collections import deque
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs():
    day=-1

    while q:
        day+=1
        qlen=len(q)

        while qlen:
            x,y,z=q.popleft()

            for i in range(6):
                nx=x+dx[i]
                ny=y+dy[i]
                nz=z+dz[i]

                if 0<=nx<h and 0<=ny<n and 0<=nz<m:
                    if arr[nx][ny][nz]==0 and check[nx][ny][nz]==0:
                        q.append((nx,ny,nz))
                        arr[nx][ny][nz] = 1
                        check[nx][ny][nz]=check[x][y][z]+1
            qlen-=1

    for k in range(h):
        for i in range(n):
            for j in range(m):
                if arr[k][i][j]==0:
                    return -1
    return day



if __name__ == '__main__':
    m,n,h=map(int,input().split())
    arr=[[list(map(int,input().split()))for _ in range(n)]for _ in range(h)]
    check=[[[0]*m for _ in range(n)]for _ in range(h)]

    q=deque()

    for k in range(h):
        for i in range(n):
            for j in range(m):
                if arr[k][i][j]==1 and check[k][i][j]==0:
                    q.append((k,i,j))
                    check[k][i][j]=1

    print(bfs())

