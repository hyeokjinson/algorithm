import sys
sys.setrecursionlimit(100000)

dx=[1,0,-1,0]
dy=[0,-1,0,1]

def dfs(x,y):
    global cnt

    cnt+=1
    visit[x][y]=True

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0<=nx<m and 0<=ny<n and arr[nx][ny]==0:
            if not visit[nx][ny]:
                dfs(nx,ny)
if __name__ == '__main__':
    m,n,k=map(int,input().split())
    arr=[[0]*n for _ in range(m)]
    visit=[[False]*n for _ in range(m)]

    for i in range(k):
        x1,y1,x2,y2=map(int,input().split())
        for j in range(x1,x2):
            for t in range(y1,y2):
                arr[t][j]=1
    res=[]

    for i in range(m):
        for j in range(n):
            if arr[i][j]==0 and visit[i][j]==False:
                cnt=0
                dfs(i,j)
                res.append(cnt)
    res.sort()
    print(len(res))
    for x in res:
        print(x,end=' ')
