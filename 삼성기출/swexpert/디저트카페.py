dx=[1,1,-1,-1]
dy=[1,-1,-1,1]

def dfs(x,y,k,cnt):
    global max_

    if k==3 and x==s_x and y==s_y:
        if max_<cnt:
            max_=cnt
    elif x<0 or x>=n or y<0 or y>=n:
        return
    elif arr[x][y] in check:
        return
    else:
        check.append(arr[x][y])

        if k==0 or k==1:
            dfs(x+dx[k],y+dy[k],k,cnt+1)
            dfs(x+dx[k+1],y+dy[k+1],k+1,cnt+1)
        elif k==2:
            if x+y!=s_x+s_y:
                dfs(x+dx[2],y+dy[2],k,cnt+1)
            else:
                dfs(x+dx[3],y+dy[3],k+1,cnt+1)
        else:
            dfs(x+dx[3],y+dy[3],k,cnt+1)
        check.remove(arr[x][y])


if __name__ == '__main__':
    T=int(input())

    for idx in range(1,T+1):
        n=int(input())
        arr=[list(map(int,input().split()))for _ in range(n)]
        max_=-2147000000

        check=[]
        for i in range(n):
            for j in range(1,n-1):
                s_x=i
                s_y=j
                check.append(arr[i][j])
                dfs(i+1,j+1,0,1)
                check.remove(arr[i][j])
        if max_==-2147000000:
            print("#{} {}".format(idx,-1))
        else:
            print("#{} {}".format(idx, max_))