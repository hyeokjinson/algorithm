n,x=map(int,input().split())
arr=list(map(int,input().split()))
result=[]
for i in arr:
    if i<x:
        result.append(i)

print(result)