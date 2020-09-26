from _collections import deque
import copy

def bfs():
    dx=[1,0,-1,0]
    dy=[0,-1,0,1]
    q=[]
    for i in range(n):
        for j in range(n):
            for t in range(1,k+1):
                if arr[i][j]==t:
                    q.append((t,0,i,j))
    q.sort()
    q=deque(q)
    while q:

        virus_value,start_time,x,y=q.popleft()
        if start_time==sec:
            return
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if arr[nx][ny]==0:
                    arr[nx][ny]=virus_value
                    q.append((virus_value,start_time+1,nx,ny))


n,k=map(int,input().split())
arr=[list(map(int,input().split()))for _ in range(n)]
sec,e_x,e_y=map(int,input().split())
bfs()
print(arr[e_x-1][e_y-1])