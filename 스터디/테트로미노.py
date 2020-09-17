dx=[0,0,1,-1]
dy=[-1,1,0,0]

l_dx=[[0,0,0,1],[0,1,2,1],[0,0,0,-1],[0,-1,0,1]]
l_dy=[[0,1,2,1],[0,0,0,1],[0,1,2,1],[0,1,1,1]]

def dfs(x,y,sum_,L):
    global res
    if L>=4:
        res=max(res,sum_)
    else:
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if ch[nx][ny]==0:
                    ch[nx][ny]=1
                    dfs(nx,ny,sum_+arr[nx][ny],L+1)
                    ch[nx][ny]=0

def another_dfs(x,y):
    global res
    for i in range(4):
        sum_=0
        ch=False
        for j in range(4):
            nx=x+l_dx[i][j]
            ny=y+l_dy[i][j]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                ch=True
                break
            else:
                sum_+=arr[nx][ny]
        if not ch:
            res=max(res,sum_)


if __name__=="__main__":
    n,m=map(int,input().split())
    arr=[list(map(int,input().split()))for _ in range(n)]
    res=-217000000
    ch=[[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            ch[i][j]=1
            dfs(i,j,arr[i][j],1)
            ch[i][j]=0

            another_dfs(i,j)
    print(res)