def dfs(check,core2,line2):
    global core
    global line

    if check==s:

        if core<core2:
            core=core2
            line=line2
        elif core2==core:
            if line>line2:
                line=line2
        return

    x=cores[check][0]
    y=cores[check][1]

    for i in range(4):
        if i==0:
            flag=0

            for i in range(x,0,-1):
                if arr[i-1][y]==1:
                    flag=1
                    break
            if flag:
                continue
            else:
                for i in range(x,0,-1):
                    arr[i-1][y]=1
                    line2+=1
                dfs(check+1,core2+1,line2)
                for i in range(x,0,-1):
                    arr[i-1][y]=0
                    line2-=1
        elif i==1:
            flag=0
            for i in range(y,n-1):
                if arr[x][i+1]==1:
                    flag=1
                    break
            if flag:
                continue
            else:
                for i in range(y,n-1):
                    arr[x][i+1]=1
                    line2+=1
                dfs(check+1,core2+1,line2)
                for i in range(y,n-1):
                    arr[x][i+1]=0
                    line2-=1
        elif i==2:
            flag=0
            for i in range(x,n-1):
                if arr[i+1][y]==1:
                    flag=1
                    break
            if flag:
                continue
            else:
                for i in range(x,n-1):
                    arr[i+1][y]=1
                    line2+=1
                dfs(check+1,core2+1,line2)
                for i in range(x,n-1):
                    arr[i+1][y]=0
                    line2-=1
        elif i==3:
            flag=0
            for i in range(y,0,-1):
                if arr[x][i-1]==1:
                    flag=1
                    break
            if flag:
                continue
            else:
                for i in range(y,0,-1):
                    arr[x][i-1]=1
                    line2+=1
                dfs(check+1,core2+1,line2)
                for i in range(y,0,-1):
                    arr[x][i-1]=0
                    line2-=1
    dfs(check+1,core2,line2)

if __name__ == '__main__':
    t=int(input())

    for k in range(t):
        cores=[]
        core=0
        line=0
        n=int(input())
        arr=[list(map(int,input().split()))for _ in range(n)]

        for i in range(1,n-1):
            for j in range(1,n-1):
                if arr[i][j]==1:
                    cores.append((i,j))
        s=len(cores)
        dfs(0,0,0)

        print("#{} {}".format(k+1,line))