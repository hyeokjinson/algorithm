def check(mid):
    ep=arr[0]
    cnt=1
    for i in range(1,n):
        if arr[i]-ep>=mid:
            cnt+=1
            ep=arr[i]
    return cnt


n,m=map(int,input().split())
arr=[]
for _ in range(n):
    arr.append(int(input()))
arr.sort()
start=0
end=max(arr)
res=0
while start<=end:
    mid = (start + end) // 2
    if check(mid)>=m:
        res=mid
        start = mid + 1
    else:
        end = mid - 1
print(res)