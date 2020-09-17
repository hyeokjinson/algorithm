from _collections import deque

dx=[1,0,-1,0]
dy=[0,-1,0,1]
n,m=map(int,input().split())
arr=[list(map(str,input().rstrip()))for _ in range(n)]
visit=[[[[False]*m for _ in range(n)]for _ in range(m)]for _ in range(n)]
cnt=0
q=deque()

def location():
    rx,ry,bx,by=0,0,0,0
    for i in range(n):
        for j in range(m):
            if arr[i][j]=='R':
                rx,ry=i,j
            elif arr[i][j]=='B':
                bx,by=i,j
    q.append((rx,ry,bx,by,1))
    visit[rx][ry][bx][by]=True

def move(x,y,dx,dy):
    cnt=0
    while arr[x+dx][y+dy]!='#' and arr[x][y]!='O':
        x+=dx
        y+=dy
        cnt+=1
    return x,y,cnt

def bfs():
    location()
    while q:
        rx,ry,bx,by,dp=q.popleft()
        if dp>10:
            break
        for i in range(4):
            nrx,nry,rcnt=move(rx,ry,dx[i],dy[i])
            nbx,nby,bcnt=move(bx,by,dx[i],dy[i])
            if arr[nbx][nby]!='O':
                if arr[nrx][nry]=='O':
                    print(dp)
                    return
                if nrx==nbx and nby==nry:
                    if rcnt>bcnt:
                        nrx-=dx[i]
                        nry-=dy[i]
                    else:
                        nbx-=dx[i]
                        nby-=dy[i]
                if not visit[nrx][nry][nbx][nby]:
                    visit[nrx][nry][nbx][nby]=True
                    q.append((nrx,nry,nbx,nby,dp+1))
    print(-1)

bfs()