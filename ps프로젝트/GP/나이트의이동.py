from collections import deque
dx=[-2,-1,1,2,2,1,-1,-2]
dy=[-1,-2,-2,-1,1,2,2,1]
def bfs():
    q.append((s_x,s_y))
    arr[s_x][s_y]=0
    while q:
        x,y=q.popleft()
        if x==e_x and y==e_y:
            return arr[x][y]

        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<l and 0<=ny<l:
                if arr[nx][ny]==0:
                    arr[nx][ny]=arr[x][y]+1
                    q.append((nx,ny))
    return 0

if __name__ == '__main__':
    T=int(input())

    for _ in range(T):
        l=int(input())
        s_x,s_y=map(int,input().split())
        e_x,e_y=map(int,input().split())

        arr=[[0]*l for _ in range(l)]

        q=deque()
        print(bfs())