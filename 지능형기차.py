result=0
arr=[]
for _ in range(4):
    n,m=map(int,input().split())
    result+=m
    result-=n
    arr.append(result)

print(max(arr))
