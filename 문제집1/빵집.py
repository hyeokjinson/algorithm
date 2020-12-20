dx=[-1,0,1]
dy=[1,1,1]

def dfs(x,y):
    global cnt
    if y==c-1:
        return True
    else:
        for i in range(3):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<r and 0<=ny<c and board[nx][ny]=='.' and visit[nx][ny]==False:
                visit[nx][ny]=True
                if dfs(nx,ny):
                    return True
    return False


if __name__ == '__main__':
    r,c=map(int,input().split())
    board=[list(map(str,input().rstrip()))for _ in range(r)]
    visit=[[False]*c for _ in range(r)]
    cnt=0

    for i in range(r):
        if board[i][0]=='.':
            if dfs(i,0):
                cnt+=1

    print(cnt)