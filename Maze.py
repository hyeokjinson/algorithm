##1. 현재위치는 출발점 (0,0)이다
#현재 위치에 방문했다는 표시를 한다.
#2.현재위치가 출구라면 종료한다.
# 3.현재 위치에서 북,동,남,서 4방향에 대해서 순서대로
# 1)그 방향으로 이동할 수 있는지(즉 벽이 아니고,미로의 외부도 아니고,이미 방문한 위치도 아닌지)검사한다
# 4.만약 둘중 어느쪽도 가지 못했다면 현재 위치에 도달하기 직전 위치로 돌아간다
# **만약 갈수 있으면 현재 위치를 스택에 push 하고 그방향으로 이동한다.
# 어느쪽으로 갈 수 없다면 스택에서 pop 한 후 그 위치로 돌아간#
import queue
#입력
n,m=map(int,input().split())
maze=[list(map(int,input())) for _ in range(n)]
dx=[-1,0,1,0]
dy=[0,1,0,-1]
chk=[[0]*m for _ in range(n)]
q=queue.Queue()
q.put([0,0])
chk[0][0]=1
while not q.empty():
    x,y=q.get()

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if nx<0 or nx>=n: continue
        if ny<0 or ny>=m: continue
        if maze[nx][ny]==0: continue
        if chk[nx][ny] !=0: continue
        chk[nx][ny]=chk[x][y]+1
        q.put([nx,ny])
print(chk[n-1][m-1])


