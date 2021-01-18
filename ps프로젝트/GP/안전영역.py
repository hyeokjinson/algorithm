import sys
sys.setrecursionlimit(10000000)
input=sys.stdin.readline

dx=[1,0,-1,0]
dy=[0,-1,0,1]

def dfs(x,y,h):
    visit[x][y]=1

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0<=nx<n and 0<=ny<n and arr[nx][ny]>h and visit[nx][ny]==0:
            dfs(nx,ny,h)

if __name__ == '__main__':
    n=int(input())

    arr=[]
    max_h=-2147000000


    for i in range(n):
        s=list(map(int,input().split()))
        max_h=max(max_h,max(s))
        arr.append(s)
    res=0
    for h in range(max_h):
        visit = [[0] * n for _ in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(n):
                if arr[i][j]>h and visit[i][j]==0:
                    cnt+=1
                    dfs(i,j,h)

        res=max(res,cnt)
        if cnt==0:
            break
    print(res)
