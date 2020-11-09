from _collections import deque

def bfs(x,y):
    dx=[1,0,-1,0]
    dy=[0,-1,0,1]
    arr[x][y] = 1
    q=deque()
    q.append([x,y])
    cnt=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<m and 0<=ny<n:
                if arr[nx][ny]==0:
                    arr[nx][ny]=1
                    q.append([nx,ny])
                    cnt+=1
    res.append(cnt)



if __name__ == '__main__':
    m,n,k=map(int,input().split())
    arr=[[0]*n for _ in range(m)]

    for i in range(k):
        x1,y1,x2,y2=map(int,input().split())
        for j in range(x1,x2):
            for k in range(y1,y2):
                arr[k][j]=1
    res = []
    for i in range(m):
        for j in range(n):
           if arr[i][j]==0:
               bfs(i,j)
    print(len(res))
    res.sort()
    for x in res:
        print(x,end=' ')
