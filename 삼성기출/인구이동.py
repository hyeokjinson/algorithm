from collections import deque

dx=[1,0,-1,0]
dy=[0,-1,0,1]

def bfs(x,y,index):
    q=deque()
    united=[]
    united.append((x,y))
    q.append((x,y))
    sum_=arr[x][y]
    ch[x][y]=index
    count=1

    while q:
        x,y=q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and ch[nx][ny]==-1:
                if l<=abs(arr[x][y]-arr[nx][ny])<=r:
                    united.append((nx,ny))
                    q.append((nx,ny))
                    ch[nx][ny]=index
                    sum_+=arr[nx][ny]
                    count+=1
    for x,y in united:
        arr[x][y]=sum_//count


if __name__ == '__main__':
    n,l,r=map(int,input().split())
    arr=[list(map(int,input().split()))for _ in range(n)]
    ans=0
    while True:
        ch=[[-1]*n for _ in range(n)]
        index=0

        for i in range(n):
            for j in range(n):
                if ch[i][j]==-1:
                    bfs(i,j,index)
                    index+=1
        if index==n*n:
            break
        ans+=1
    print(ans)