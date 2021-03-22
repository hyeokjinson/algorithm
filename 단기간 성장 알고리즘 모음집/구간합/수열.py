def solve(n,k,arr):
    temp=sum(arr[:k])
    ans=temp

    for i in range(k,n):
        temp+=arr[i]
        temp-=arr[i-k]
        if temp>ans:
            ans=temp
    return ans if n!=k else temp

def solve1(n,k,arr):
    prefix_sum=[0]
    summary=0
    for i in arr:
        summary+=i
        prefix_sum.append(summary)

    res=-2147000000
    for i in range(1,n-k+1):
        temp=prefix_sum[i+k]-prefix_sum[i]
        if temp>res:
            res=temp
    return res if n!=k else sum(arr[:k])



if __name__ == '__main__':
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))

    print(solve1(n,k,arr))
