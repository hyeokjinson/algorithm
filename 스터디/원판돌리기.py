from _collections import deque
dx=[1,0,-1,0]
dy=[0,-1,0,1]
def rotate(x,d,k):
    for i in range(x-1,n,x):
        temp=[]
        for j in range(m):
            #시계
            if d==1:
                temp.append(arr[i][(j+k)%m])
            #반시계
            elif d==0:
                temp.append(arr[i][(m+j-k)%m])
        arr[i]=temp[:]

def bfs(x,y):
    q=deque()
    q.append((x,y))
    visit[x][y]=1
    res=False
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=(y+dy[i])%m

            if nx < 0 or ny < 0 or nx > n - 1 or ny > m - 1 or visit[nx][ny] or arr[x][y] != arr[nx][ny] or arr[nx][ny] == 0: continue
            q.append((nx,ny))
            visit[nx][ny]=1
            res=True
    if res:
        return True
    else:
        visit[x][y]=0
        return False

def solve(x,d,k):
    flag=False
    rotate(x,d,k)
    sum_,cnt=0,0
    for i in range(n):
        for j in range(m):
            if arr[i][j]:
                cnt+=1
                sum_+=arr[i][j]
            if visit[i][j]==0 and arr[i][j]:
                if bfs(i,j):
                    flag=True
    if cnt!=0:
        avg=sum_/cnt
    else:
        return
    for i in range(n):
        for j in range(m):
            if flag:
                if visit[i][j]:
                    arr[i][j]=0
            else:
                if arr[i][j] and arr[i][j]>avg:
                    arr[i][j]-=1
                elif arr[i][j] and arr[i][j]<avg:
                    arr[i][j]+=1





if __name__ == '__main__':
    n,m,t=map(int,input().split())
    arr=[list(map(int,input().split()))for _ in range(n)]
    for _ in range(t):
        x,d,k=map(int,input().split())
        visit=[[0]*m for _ in range(n)]
        solve(x,d,k)
    res=0
    for i in range(n):
        res+=sum(arr[i])
    print(res)