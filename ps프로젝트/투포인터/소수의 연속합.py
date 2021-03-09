import sys

input=sys.stdin.readline

if __name__ == '__main__':
    n=int(input())
    isPrime=[False,False]+[True]*(n-1)
    arr=[]


    for i in range(2,n+1):
        if isPrime[i]:
            arr.append(i)
        for j in range(2*i,n+1,i):
            isPrime[j]=False

    count=0
    end=0
    interval_sum=0
    for start in range(len(arr)):
        while interval_sum<n and end<len(arr):
            interval_sum+=arr[end]
            end+=1

        if interval_sum==n:
            count+=1
        interval_sum-=arr[start]
    print(count)