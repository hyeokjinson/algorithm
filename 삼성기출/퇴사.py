
def dfs(L,sum_):
    global res

    if L==n-1:
        res=max(res,sum_)
    else:
        if L+pt[L]<n+1:
            dfs(L+pt[L],sum_+p[L])
        dfs(L+1,sum_)

if __name__ == '__main__':
    n=int(input())
    pt=[]
    p=[]
    res=-2147000000
    for _ in range(n):
        a,b=map(int,input().split())
        pt.append(a)
        p.append(b)
    dfs(0,0)
    print(res)