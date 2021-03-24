from collections import deque

if __name__ == '__main__':
    t=int(input())
    directions={
        0:(),
        1:((1,0),(0,1),(0,-1),(-1,0)),
        2:((1,0),(-1,0)),
        3:((0,1),(0,-1)),
        4:((-1,0),(0,1)),
        5:((1,0),(0,1)),
        6:((1,0),(0,-1)),
        7:((-1,0),(0,-1))
    }

    for i in range(1,t+1):
        n,m,r,c,l=map(int,input().split())
        maps=[list(map(int,input().split()))for _ in range(n)]
        visit=[[0 for _ in range(m)]for _ in range(n)]
        visit[r][c]=1
        cnt=1

        q=deque()
        q.append((r,c))

        while q:
            x,y=q.popleft()

            for dx,dy in directions[maps[x][y]]:
                nx=x+dx
                ny=y+dy
                if not 0<=nx<n or not 0<=ny<m:
                    continue
                if (-dx,-dy) in directions[maps[nx][ny]]:
                    if not visit[nx][ny]:
                        visit[nx][ny]=visit[x][y]+1
                        q.append((nx,ny))

                        if visit[nx][ny]<=l:
                            cnt+=1
        print("#{} {}".format(i,cnt))