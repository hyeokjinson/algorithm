n,m=map(int,input().split())
arr=[list(map(int,input().split()))for _ in range(n)]
res=-217000000
for i in arr:
    x=min(i)
    res=max(x,res)
print(res)