import copy

def dfs(L):
    global min_,arr
    if L==len(pos):
        sum_=0
        for i in range(n):
            for j in range(m):
                if arr[i][j]==0:
                    sum_+=1
        min_=min(min_,sum_)
    else:
        value,x,y=pos[L]
        temp = copy.deepcopy(arr)
        if value==1:
            for i in range(x-1,-1,-1):    #상
                if arr[i][y]==0:
                    arr[i][y]='#'
                elif arr[i][y]==6:
                    break
            dfs(L+1)

            arr = copy.deepcopy(temp)
            for i in range(x+1,n):
                if arr[i][y]==0:          #하
                    arr[i][y]='#'
                elif arr[i][y]==6:
                    break
            dfs(L+1)
            arr = copy.deepcopy(temp)
            for i in range(y-1,-1,-1):
                if arr[x][i]==0:
                    arr[x][i]='#'
                elif arr[x][i]==6:           #좌
                    break
            dfs(L+1)
            arr = copy.deepcopy(temp)
            for i in range(y+1,m):
                if arr[x][i] == 0:
                    arr[x][i] = '#'      #우
                elif arr[x][i] == 6:
                    break
            dfs(L + 1)
        elif value==2:
            for i in range(x-1,-1,-1):    #상
                if arr[i][y]==0:
                    arr[i][y]='#'
                elif arr[i][y]==6:
                    break
            for i in range(x + 1, n):
                if arr[i][y] == 0:  # 하
                    arr[i][y] = '#'
                elif arr[i][y] == 6:
                    break
            dfs(L+1)
            arr = copy.deepcopy(temp)
            for i in range(y - 1, -1, -1):
                if arr[x][i] == 0:
                    arr[x][i] = '#'
                elif arr[x][i] == 6:  # 좌
                    break
            for i in range(y+1,m):
                if arr[x][i] == 0:
                    arr[x][i] = '#'      #우
                elif arr[x][i] == 6:
                    break
            dfs(L + 1)

        elif value==3:
            for i in range(x-1,-1,-1):    #상
                if arr[i][y]==0:
                    arr[i][y]='#'
                elif arr[i][y]==6:
                    break
            for i in range(y+1,m):
                if arr[x][i] == 0:
                    arr[x][i] = '#'      #우
                elif arr[x][i] == 6:
                    break
            dfs(L + 1)
            arr = copy.deepcopy(temp)
            for i in range(y+1,m):
                if arr[x][i] == 0:
                    arr[x][i] = '#'      #우
                elif arr[x][i] == 6:
                    break
            for i in range(x+1,n):
                if arr[i][y]==0:          #하
                    arr[i][y]='#'
                elif arr[i][y]==6:
                    break
            dfs(L + 1)
            arr = copy.deepcopy(temp)
            for i in range(x+1,n):
                if arr[i][y]==0:          #하
                    arr[i][y]='#'
                elif arr[i][y]==6:
                    break
            for i in range(y-1,-1,-1):
                if arr[x][i]==0:
                    arr[x][i]='#'
                elif arr[x][i]==6:           #좌
                    break
            dfs(L + 1)
            arr = copy.deepcopy(temp)
            for i in range(y-1,-1,-1):
                if arr[x][i]==0:
                    arr[x][i]='#'
                elif arr[x][i]==6:           #좌
                    break
            for i in range(x-1,-1,-1):    #상
                if arr[i][y]==0:
                    arr[i][y]='#'
                elif arr[i][y]==6:
                    break
            dfs(L + 1)
        elif value==4:
            for i in range(y-1,-1,-1):
                if arr[x][i]==0:
                    arr[x][i]='#'
                elif arr[x][i]==6:           #좌
                    break
            for i in range(x-1,-1,-1):    #상
                if arr[i][y]==0:
                    arr[i][y]='#'
                elif arr[i][y]==6:
                    break
            for i in range(y+1,m):
                if arr[x][i] == 0:
                    arr[x][i] = '#'      #우
                elif arr[x][i] == 6:
                    break
            dfs(L + 1)
            arr = copy.deepcopy(temp)
            for i in range(x-1,-1,-1):    #상
                if arr[i][y]==0:
                    arr[i][y]='#'
                elif arr[i][y]==6:
                    break
            for i in range(y+1,m):
                if arr[x][i] == 0:
                    arr[x][i] = '#'      #우
                elif arr[x][i] == 6:
                    break
            for i in range(x+1,n):
                if arr[i][y]==0:          #하
                    arr[i][y]='#'
                elif arr[i][y]==6:
                    break
            dfs(L + 1)
            arr = copy.deepcopy(temp)
            for i in range(y+1,m):
                if arr[x][i] == 0:
                    arr[x][i] = '#'      #우
                elif arr[x][i] == 6:
                    break
            for i in range(x+1,n):
                if arr[i][y]==0:          #하
                    arr[i][y]='#'
                elif arr[i][y]==6:
                    break
            for i in range(y-1,-1,-1):
                if arr[x][i]==0:
                    arr[x][i]='#'
                elif arr[x][i]==6:           #좌
                    break
            dfs(L + 1)
            arr = copy.deepcopy(temp)
            for i in range(x+1,n):
                if arr[i][y]==0:          #하
                    arr[i][y]='#'
                elif arr[i][y]==6:
                    break
            for i in range(y-1,-1,-1):
                if arr[x][i]==0:
                    arr[x][i]='#'
                elif arr[x][i]==6:           #좌
                    break
            for i in range(x-1,-1,-1):    #상
                if arr[i][y]==0:
                    arr[i][y]='#'
                elif arr[i][y]==6:
                    break
            dfs(L+1)
        else:
            for i in range(x-1,-1,-1):    #상
                if arr[i][y]==0:
                    arr[i][y]='#'
                elif arr[i][y]==6:
                    break
            for i in range(x+1,n):
                if arr[i][y]==0:          #하
                    arr[i][y]='#'
                elif arr[i][y]==6:
                    break
            for i in range(y-1,-1,-1):
                if arr[x][i]==0:
                    arr[x][i]='#'
                elif arr[x][i]==6:           #좌
                    break
            for i in range(y+1,m):
                if arr[x][i] == 0:
                    arr[x][i] = '#'      #우
                elif arr[x][i] == 6:
                    break
            dfs(L+1)

if __name__=="__main__":
    n,m=map(int,input().split())
    arr=[list(map(int,input().split()))for _ in range(n)]
    pos=[]
    for i in range(n):
        for j in range(m):
            if arr[i][j]!=0 and arr[i][j]!=6:
                pos.append((arr[i][j],i,j))
    min_=217000000
    dfs(0)
    print(min_)
