dx=[1,0,-1,0]
dy=[0,-1,0,1]

def dfs(x,y):
    global cnt

    cnt+=1
    visit[x][y]=True
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0<=nx<n and 0<=ny<n and arr[nx][ny]==1:
            if not visit[nx][ny]:
                dfs(nx,ny)
if __name__ == '__main__':
    n=int(input())
    arr=[list(map(int,input().rstrip())) for _ in range(n)]
    visit=[[False]*n for _ in range(n)]
    res=[]
    for i in range(n):
        for j in range(n):
            if arr[i][j]==1 and visit[i][j]==False:
                cnt=0
                dfs(i,j)
                res.append(cnt)
    print(len(res))
    res.sort()
    for x in res:
        print(x)