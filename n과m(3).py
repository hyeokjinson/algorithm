N,M=map(int,input().split())
a=[0 for i in range(M)]
def dfs(number,index,N,M):
    if index==M:
        print(' '.join(map(str,a)))
        return
    if number>N:
        return
    a[index]=number
    dfs(number,index+1,N,M)
    a[index]=0
    dfs(number+1,index,N,M)


dfs(1,0,N,M)
