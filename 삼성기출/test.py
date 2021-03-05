def dfs(x,y,d):
    global cnt
    arr[x][y]=2
    while True:
        for i in range(4):
            res=False
            dd=(d+3)%4
            nx=x+dx[dd]
            ny=y+dy[dd]
            d=dd
            if 0<=nx<n and 0<=ny<m:
                if arr[nx][ny]==0:
                    arr[nx][ny]=2
                    cnt+=1
                    res=True
                    x=nx
                    y=ny
                    break

        if not res:
            if arr[x-dx[d]][y-dy[d]]==1:
                return
            else:
                x=x-dx[d]
                y=y-dy[d]





if __name__ == '__main__':
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    n,m=map(int,input().split())
    r,c,d=map(int,input().split())
    arr=[list(map(int,input().split()))for _ in range(n)]
    cnt=1
    dfs(r,c,d)
    print(cnt)