
def move():
    for i in range(n):
        num=i
        for j in range(h):
            if arr[num][j]:
                num+=1
            elif arr[num-1][j]:
                num-=1
        if i!=num:
            return 0
    return 1

def dfs(cnt,idx,r):
    global res
    if cnt==r:
        if move():
            res=min(res,cnt)
            return
    for i in range(idx,h):
        for j in range(n-1):
            if arr[j][i]:
                continue
            if j-1>=0 and arr[j-1][i]:
                continue
            if j+1<n and arr[j+1][i]:
                continue
            arr[j][i]=1
            dfs(cnt+1,i,r)
            arr[j][i]=0

if __name__ == '__main__':
    n,m,h=map(int,input().split())
    arr=[[0]*h for _ in range(n)]

    for _ in range(m):
        a,b=map(int,input().split())
        arr[b-1][a-1]=1
    res=-2147000000
    flag=False
    for r in range(4):
        dfs(0,0,r)
        if res!=-2147000000:
            print(res)
            flag=True
            break
    if not flag:
        print(-1)
