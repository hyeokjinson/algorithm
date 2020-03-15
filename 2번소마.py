# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import queue

T=int(input())
def dfs(maze,cnt,x,y):
    maze[x][y]=0
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if nx>=0 and nx<n and ny>=0 and ny<n:
            if maze[nx][ny]==1 and maze[x]:
                cnt=dfs(maze,cnt+1,nx,ny)
    return cnt

for _ in range(T):
    n, m = map(int, input().split())
    maze = [list(map(int, input())) for _ in range(n)]
