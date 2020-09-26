from itertools import combinations

def get_sum(cb):
    res=0
    for hx,hy in hs:
        tmp=217000000
        for cx,cy in cb:
            tmp=min(tmp,abs(hx-cx)+abs(hy-cy))
        res+=tmp
    return res

if __name__=="__main__":
    n,m=map(int,input().split())
    arr=[list(map(int,input().split()))for _ in range(n)]
    hs=[]
    chicken_store=[]

    for i in range(n):
        for j in range(n):
            if arr[i][j]==1:
                hs.append((i,j))
            if arr[i][j] == 2:
                chicken_store.append((i, j))
    cb=list(combinations(chicken_store,m))
    res=217000000
    for combi in cb:
        res=min(res,get_sum(combi))
    print(res)