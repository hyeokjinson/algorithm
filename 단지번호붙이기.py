import queue
import sys
n=int(sys.stdin.readline())
def dfs(maze,cnt,x,y):
    maze[x][y]=0 #이미 간것은 0으로 바꾸는것
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]  #상하좌우 판단

        if nx>=0 and nx<n and ny>=0 and ny<n: #범위 체크
            if maze[nx][ny]==1:           #그부분이 1이면
                cnt=dfs(maze,cnt+1,nx,ny)   #카운트 증가시켜서 다시한번 그 근처 확인
    return cnt

maze=[list(map(int,input()))for _ in range(n)]
#input값 넣기

ans=[]
for i in range(n):
    for j in range(n):
        if maze[i][j]==1:   #1일때 주변 탐색
            ans.append(dfs(maze,1,i,j))
print(len(ans))
for i in sorted(ans):
    print(i)