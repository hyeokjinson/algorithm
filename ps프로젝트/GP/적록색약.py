from collections import deque

dx=[1,0,-1,0]
dy=[0,-1,0,1]

def bfs(x,y,c,w):
    q=deque()
    q.append((x,y))
    visit[x][y]=True

    while q:
        c_x,c_y=q.popleft()

        for i in range(4):
            nx=c_x+dx[i]
            ny=c_y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n or visit[nx][ny]:
                continue
            if w and c=='B' and (arr[nx][ny]=='R' or arr[nx][ny]=='G'):
                continue
            if w and c!='B' and arr[nx][ny]=='B':
                continue
            if not w and arr[nx][ny]!=c:
                continue
            q.append((nx,ny))
            visit[nx][ny]=True

if __name__ == '__main__':
    n=int(input())
    arr=[list(input())for _ in range(n)]
    visit=[[False]*n for _ in range(n)]
    cnt=0
    for i in range(n):
        for j in range(n):
            if not visit[i][j]:
                bfs(i,j,arr[i][j],False)
                cnt+=1
    print(cnt,end=' ')
    cnt=0
    visit = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visit[i][j]:
                bfs(i,j,arr[i][j],True)
                cnt+=1
    print(cnt)