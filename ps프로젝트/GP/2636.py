from collections import deque

dx=[1,0,-1,0]
dy=[0,-1,0,1]

def bfs(left):
    while q:
        x,y=q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<n and 0<=ny<m and visit[nx][ny]==0:
                visit[nx][ny]=1

                if arr[nx][ny]==1:
                    arr[nx][ny]=2
                    left-=1
                else:
                    q.append((nx,ny))
    return left

def delete():
    for i in range(n):
        for j in range(m):
            if arr[i][j]==2:
                arr[i][j]=0

if __name__ == '__main__':
    n,m=map(int,input().split())

    arr=[list(map(int,input().split()))for _ in range(n)]

    left=0

    for i in range(n):
        for j in range(m):
            if arr[i][j]==1:
                left+=1

    cnt=0
    temp=left
    q=deque()
    while left!=0:
        visit=[[0 for _ in range(m)]for _ in range(n)]
        q.append((0,0))
        visit[0][0]=1
        left=bfs(left)
        if left!=0:
            temp=left
        delete()

        cnt+=1

    print(cnt)
    print(temp)