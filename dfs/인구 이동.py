from _collections import deque
dx=[1,0,-1,0]
dy=[0,-1,0,1]
def process(x,y,index):
    check_arr=[]
    check_arr.append((x,y))
    q=deque()
    q.append((x,y))
    ch[x][y]=index
    sum_=arr[x][y]
    cnt=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and ch[nx][ny]==-1:
                if l<=abs(arr[x][y]-arr[nx][ny])<=r:
                    ch[nx][ny]=index
                    q.append((nx,ny))
                    check_arr.append((nx,ny))
                    cnt+=1
                    sum_+=arr[nx][ny]
    for i,j in check_arr:
        arr[i][j]=sum_//cnt
    return cnt


if __name__ == '__main__':
    n,l,r=map(int,input().split())
    arr=[list(map(int,input().split()))for _ in range(n)]
    total_count=0
    while True:
        ch=[[-1]*n for _ in range(n)]
        index=0
        for i in range(n):
            for j in range(n):
                if ch[i][j]==-1:
                    process(i,j,index)
                    index+=1
        if index==n*n:
            break
        total_count+=1
    print(total_count)

