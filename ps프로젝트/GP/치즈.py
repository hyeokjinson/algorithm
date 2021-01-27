from collections import deque

dx=[1,0,-1,0]
dy=[0,-1,0,1]

def find(x,y):
    q=deque()
    q.append((x,y))
    arr[x][y]=5

    while q:
        x,y=q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0>nx or nx>=n or 0>ny or ny>=m:
                continue
            if arr[nx][ny] == 5:
                continue
            elif arr[nx][ny]==1:
                arr[nx][ny]=2
            elif arr[nx][ny]==2:
                arr[nx][ny]=3
            elif arr[nx][ny]==0:
                arr[nx][ny]=5
                q.append((nx,ny))

def melt():
    cnt=0

    for i in range(n):
        for j in range(m):
            if arr[i][j]==5:
                arr[i][j]=0
            if arr[i][j]==2:
                arr[i][j]=1
            if arr[i][j]==3:
                cnt+=1
                arr[i][j]=0
    return cnt



if __name__ == '__main__':
    n,m=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(n)]
    m_cnt=0
    time=0

    while True:
        find(0,0)
        m_cnt=melt()
        if m_cnt==0:
            break
        time+=1
    print(time)
