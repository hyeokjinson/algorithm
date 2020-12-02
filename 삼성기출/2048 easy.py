from collections import deque

n=int(input())
board=[list(map(int,input().split()))for _ in range(n)]
answer,q=0,deque()

def get(i,j):
    if board[i][j]:
        q.append(board[i][j])
        board[i][j]=0

def merge(i,j,di,dj):
    while q:
        x=q.popleft()
        if not board[i][j]:
            board[i][j]=x
        elif board[i][j]==x:
            board[i][j]=x*2
            i,j=i+di,j+dj
        else:
            i,j=i+di,j+dj
            board[i][j]=x

def move(k):
    if k==0:
        for i in range(n):
            for j in range(n):
                get(j,i)
            merge()

def solve(count):
    global board,answer

    if count==5:
        for i in range(n):
            answer=max(answer,max(board[i]))
        return

    b=[x[:] for x in board]

    for k in range(4):
        move(k)
        solve(count+1)
        board=[x[:] for x in b]

solve(0)
print(answer)