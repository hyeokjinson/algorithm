def dfs(x,y,d):
    global cnt
    while True:
        for i in range(4):
            res=False
            dd=(d+3)%4

            nx=x+dx[dd]
            ny=y+dy[dd]
            d=dd
            if arr[nx][ny]==0:
                cnt+=1
                arr[nx][ny]=3
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
    arr[r][c]=3

    dfs(r,c,d)
    print(cnt)