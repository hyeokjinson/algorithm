
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def first():
    res=[]
    for i in range(r):
        for j in range(c):
            if board[i][j]==-1:
                board[i][j]=0
            else:
                board[i][j]+=1
                if board[i][j]==3:
                    board[i][j]=-1
                    res.append([i,j])
    return res

def second(pos):
    for x,y in pos:

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<r and 0<=ny<c:
                board[nx][ny]=-1


if __name__ == '__main__':
    r,c,n=map(int,input().split())
    board=[[-1]*c for _ in range(r)]

    for i in range(r):
        row=input()
        for j in range(c):
            if row[j]=='O':
                board[i][j]=1

    if n!=1:
        t=1
        while True:
            pos=first()

            if pos:
                second(pos)
            t+=1
            if t==n:
                break

    for i in range(r):
        for j in range(c):
            if board[i][j]==-1:
                print('.',end='')
            else:
                print('O',end='')
        print()