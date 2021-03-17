from collections import deque
dx=[1,0,-1,0]
dy=[0,1,0,-1]
def bfs(x,y):
    q=deque([(x,y)])

    visit=set([(x,y)])
    ans=0
    eat_flag=False
    shark=2
    eat = 0
    time=0
    while q:
        size=len(q)
        q=deque(sorted(q))
        for _ in range(size):
            x,y=q.popleft()

            if arr[x][y]!=0 and arr[x][y]<shark:
                eat+=1
                arr[x][y]=0

                if eat==shark:
                    shark+=1
                    eat=0
                q=deque()
                visit=set([(x,y)])
                ans=time
                eat_flag=True
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<n and 0<=ny<n and (nx,ny) not in visit:
                    if arr[nx][ny]<=shark:
                        q.append((nx,ny))
                        visit.add((nx,ny))
            if eat_flag:
                eat_flag=False
                break
        time+=1
    return ans


if __name__ == '__main__':
    n=int(input())
    arr=[list(map(int,input().split()))for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if arr[i][j]==9:
                s_x,s_y=i,j
                arr[i][j]=0

    print(bfs(s_x,s_y))