def dfs(x,y,count):
    global cnt

    if count==k:
        if x==0 and y==c-1:
            cnt+=1
    else:
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<r and 0<=ny<c and arr[nx][ny]=='.':
                arr[nx][ny]='T'
                dfs(nx,ny,count+1)
                arr[nx][ny]='.'


if __name__ == '__main__':
    dx=[1,0,-1,0]
    dy=[0,-1,0,1]

    r,c,k=map(int,input().split())
    arr=[list(map(str,input().strip()))for _ in range(r)]
    arr[r-1][0]='H'
    cnt=0
    dfs(r-1,0,1)
    print(cnt)