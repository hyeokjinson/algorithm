import sys
from _collections import deque

def student_search(x,y,direction):

    if direction==0:
        while y>=0:
            if arr[x][y]=='S':
                return True
            if arr[x][y]=='O':
                return False
            y-=1
    if direction==1:
        while y<n:
            if arr[x][y]=='S':
                return True
            if arr[x][y]=='O':
                return False
            y+=1
    if direction==2:
        while x>=0:
            if arr[x][y]=='S':
                return True
            if arr[x][y]=='O':
                return False
            x-=1
    if direction==3:
        while x<n:
            if arr[x][y]=='S':
                return True
            if arr[x][y]=='O':
                return False
            x+=1
    return False


def bfs():
    q = deque()
    for i in range(n):
        for j in range(n):
            if arr[i][j]=='T':
                q.append((i,j))
    while q:
        x,y=q.popleft()
        for i in range(4):
            if student_search(x,y,i):
                return True
    return False


def setwall(wall):
    global check
    if wall==3:
        if not bfs():
            check=True
            return
    else:
        for i in range(n):
            for j in range(n):
                if arr[i][j]=='X':
                    arr[i][j]='O'
                    setwall(wall+1)
                    arr[i][j]='X'
    return False


if __name__=="__main__":
    n=int(input())
    arr=[list(map(str,input().split()))for _ in range(n)]
    check=False
    setwall(0)
    if check:
        print('YES')
    else:
        print('NO')