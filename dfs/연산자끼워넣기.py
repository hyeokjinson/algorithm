def dfs(L,add,sub,div,mul,sum_):
    global max_,min_

    if L==n:
        max_=max(sum_,max_)
        min_=min(sum_,min_)
        return
    else:
        if add:
            dfs(L+1,add-1,sub,div,mul,sum_+num[L])
        if sub:
            dfs(L + 1, add , sub- 1, div, mul, sum_-num[L])
        if div:
            dfs(L + 1, add, sub , div- 1, mul, sum_*num[L])
        if mul:
            dfs(L + 1, add, sub, div , mul- 1, int(sum_/num[L]))
n=int(input())
num=list(map(int,input().split()))
add,sub,div,mul=map(int,input().split())
max_=-217000000
min_=217000000
dfs(1,add,sub,div,mul,num[0])
print(max_)
print(min_)