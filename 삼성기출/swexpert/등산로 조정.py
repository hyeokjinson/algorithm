from collections import deque

def dfs(x,y,cnt,k,n):
    global res
    if res<cnt+1:
        res=cnt+1
    visit[x][y]=1
    dx=[1,0,-1,0]
    dy=[0,-1,0,1]

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n and visit[nx][ny]==0:
            if maps[nx][ny]<maps[x][y]:
                dfs(nx,ny,cnt+1,k,n)
            elif maps[nx][ny]-k<maps[x][y]:
                tmp=maps[nx][ny]
                maps[nx][ny]=maps[x][y]-1
                dfs(nx,ny,cnt+1,0,n)
                maps[nx][ny]=tmp
    visit[x][y]=0



if __name__ == '__main__':
    T=int(input())
    idx=1
    for _ in range(T):
        n,k=map(int,input().split())
        maps=[]
        max_=-2147000000
        res=-2147000000
        for i in range(n):
            tmp=list(map(int,input().split()))
            max_=max(max(tmp),max_)
            maps.append(tmp)

        start=[]
        for i in range(n):
            for j in range(n):
                if maps[i][j]==max_:
                    start.append((i,j))
        visit=[[0]*n for _ in range(n)]

        for x,y in start:
            dfs(x,y,0,k,n)

        print("#{} {}".format(idx,res))
        idx+=1
