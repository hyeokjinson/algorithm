from collections import deque


if __name__ == '__main__':
    t=int(input())

    dx=[0,-1,1,0,0]
    dy=[0,0,0,-1,1]

    for idx in range(1,t+1):
        n,m,k=map(int,input().split())
        board=[list(map(int,input().split()))for _ in range(n)]

        for q in range(m):
            cnt=-1
            visit=[[0]*n for _ in range(n)]

            for w in board:
                cnt+=1
                x,y,num,dir=w
                if num>0:
                    nx=x+dx[dir]
                    ny=y+dy[dir]

                    if nx==0 or nx==n-1 or ny==0 or ny==n-1:
                        num=num//2
                        dir=(dir+3)%4
                    else:
                        if visit[nx][ny]==0:
                            visit[nx][ny]=[num,num,cnt]
                        else:
                            if visit[nx][ny][1]>num:
                                visit[nx][ny][0]+=num
                                board[visit[nx][ny][2]][2]=visit[nx][ny][0]
                                num=0
                            else:
                                visit[nx][ny][0]+=num
                                visit[nx][ny][1]=num
                                board[visit[nx][ny][2]][2]=0
                                visit[nx][ny][2]=cnt
                                num=visit[nx][ny][0]
                    x=nx
                    y=ny
        num_sum=0
        for e in board:
            num_sum+=e[2]
        print("#{} {}".format(idx,num_sum))




