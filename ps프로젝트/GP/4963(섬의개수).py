from collections import deque

dx=[1,0,-1,0,-1,-1,1,1]
dy=[0,-1,0,1,-1,1,-1,1]

def bfs(x,y):
    q=deque()
    q.append((x,y))
    visit[x][y]=True

    while q:
        c_x,c_y=q.popleft()

        for i in range(8):
            nx=c_x+dx[i]
            ny=c_y+dy[i]
            if 0<=nx<h and 0<=ny<w and arr[nx][ny]==1:
                if not visit[nx][ny]:
                    visit[nx][ny]=True
                    q.append((nx,ny))

if __name__ == '__main__':
    while True:
        w,h=map(int,input().split())

        if w==0 and h==0:
            break

        arr=[list(map(int,input().split())) for _ in range(h)]
        visit=[[False]*w for _ in range(h)]
        cnt=0
        for i in range(h):
            for j in range(w):
                if arr[i][j]==1 and not visit[i][j]:
                    cnt+=1
                    bfs(i,j)
        print(cnt)