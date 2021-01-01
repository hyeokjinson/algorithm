from _collections import deque

dx=[-1,-2,-2,-1,1,2,2,1]
dy=[-2,-1,1,2,2,1,-1,-2]

if __name__ == '__main__':
    t=int(input())

    for _ in range(t):
        l=int(input())
        x,y=map(int,input().split())
        d_x,d_y=map(int,input().split())
        dis=[[0]*l for _ in range(l)]
        q=deque()
        dis[x][y]=0
        q.append((x,y))
        while q:
            s_x,s_y=q.popleft()

            if s_x==d_x and s_y==d_y:
                break

            for i in range(8):
                nx=s_x+dx[i]
                ny=s_y+dy[i]
                if 0<=nx<l and 0<=ny<l and dis[nx][ny]==0:
                    dis[nx][ny]=dis[s_x][s_y]+1
                    q.append((nx,ny))
        print(dis[d_x][d_y])

