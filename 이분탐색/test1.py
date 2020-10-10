def Count(len):
    cnt=1
    ep=arr[0]
    for i in range(1,n):
        if arr[i]-ep>=len:
            cnt+=1
            ep=arr[i]
    return cnt


n,c=map(int,input().split())
arr=[]
for _ in range(n):
    arr.append(int(input()))
arr.sort()
start=1
end=arr[n-1]
res=0
while start<=end:
    mid=(start+end)//2
    if Count(mid)>=c:
        res=mid
        start=mid+1
    else:
        end=mid-1
print(res)