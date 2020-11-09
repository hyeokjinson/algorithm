dx=[1,0,-1,0]
dy=[0,1,0,-1]

def dfs(x,y):
    global cnt
    cnt+=1
    board[x][y]=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m and board[nx][ny]==0:
            dfs(nx,ny)

if __name__ == '__main__':
    n,m=map(int,input().split())
    board=[list(map(int,input().split()))for _ in range(n)]
    res=[]
    for i in range(n):
        for j in range(m):
            if board[i][j]==0:
                cnt=0
                dfs(i,j)
                res.append(cnt)
    print(len(res))