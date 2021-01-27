if __name__ == '__main__':
    k,n=map(int,input().split())
    arr=[]
    for _ in range(k):
        arr.append(int(input()))

    arr.sort()

    start=1
    end=arr[-1]

    while start<=end:

        mid=(start+end)//2
        count=0
        for x in arr:
            if x>=mid:
                count+=x//mid

        if count>=n:
            start=mid+1
        else:
            end=mid-1

    print(end)


