from _collections import deque
import sys
dx=[1,0,-1,0]
dy=[0,1,0,-1]

def bfs(s_x,s_y,e_x,e_y,f):
    global c
    sum_=0
    dis=[[0]*n for _ in range(n)]
    q=deque()
    q.append((s_x,s_y))
    dis[s_x][s_y]=0
    while q:
        tmp=q.popleft()
        if tmp[0]==e_x-1 and tmp[1]==e_y-1:
            if dis[tmp[0]][tmp[1]]<=f:
                return dis[tmp[0]][tmp[1]]

        for i in range(4):
            nx=tmp[0]+dx[i]
            ny=tmp[1]+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if arr[nx][ny]==0:
                    if dis[nx][ny]==0:

                        dis[nx][ny]=dis[tmp[0]][tmp[1]]+1
                        q.append((nx,ny))

    return -1
def f_info(x,y):
    f_q=[]
    q=deque(ps)

    for i in range(m):
        if q:
            tmp=q.popleft()
            v=bfs(x,y,tmp[0],tmp[1])
            f_q.append([tmp[0],tmp[1],tmp[2],tmp[3],v])

    f_q=sorted(f_q,key=lambda x:x[-1])
    return f_q[0]


if __name__=="__main__":
    n,m,c=map(int,input().split())
    arr=[list(map(int,input().split()))for _ in range(n)]
    t_s_x,t_s_y=map(int,input().split())
    ps=[]
    for _ in range(m):
        s_x1,s_y1,e_x1,e_y1=map(int,input().split())
        ps.append([s_x1-1,s_y1-1,e_x1-1,e_y1-1])
    while ps:
        tmp=ps.pop(ps.index(f_info(t_s_x-1,t_s_y-1)[:-1]))



