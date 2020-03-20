N,M=map(int,input().split())
a=[0 for i in range(M)]
def dfs(index,N,M):
    if index==M:
        print(' '.join(map(str,a)))
        return
    for i in range(1,N+1):
        a[index]=i
        dfs(index+1,N,M)

dfs(0,N,M)
