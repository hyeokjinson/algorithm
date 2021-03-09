if __name__ == '__main__':
    n,s=map(int,input().split())
    arr=list(map(int,input().split()))

    interval_sum=arr[0]
    end=0
    min_=2147000000

    for start in range(n):
        while interval_sum<s and end<n:
            end+=1
            if end==n:
                break
            interval_sum += arr[end]

        if interval_sum>=s:
            res=end-start+1
            min_=min(min_,res)
        interval_sum-=arr[start]

    if min_==2147000000:
        print(0)
    else:
        print(min_)