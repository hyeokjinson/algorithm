
def dfs(L,add,sub,mul,div,sum_):
    global max_,min_
    if L==n:
        max_=max(sum_,max_)
        min_=min(sum_,min_)
        return
    else:
        if add:
            dfs(L+1,add-1,sub,mul,div,sum_+arr[L])
        if sub:
            dfs(L + 1,  add, sub-1, mul, div, sum_ - arr[L])
        if mul:
            dfs(L + 1, add , sub, mul-1, div, sum_ * arr[L])
        if div:
            dfs(L + 1, add , sub, mul, div-1, int(sum_ /arr[L]))

if __name__ == '__main__':
    n=int(input())
    arr=list(map(int,input().split()))
    add,sub,mul,div=map(int,input().split())
    max_=-2147000000
    min_=2147000000

    dfs(1,add,sub,mul,div,arr[0])
    print(max_)
    print(min_)