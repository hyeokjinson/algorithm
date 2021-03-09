if __name__ == '__main__':
    n,m=map(int,input().split())
    a=list(map(int,input().split()))

    count=0
    end=0
    interval_sum=0

    for start in range(n):
        while interval_sum<m and end<n:
            interval_sum+=a[end]
            end+=1

        if interval_sum==m:
            count+=1
        interval_sum-=a[start]
    print(count)