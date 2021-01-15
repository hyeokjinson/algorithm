import heapq


if __name__ == '__main__':
    k,n=map(int,input().split())
    arr=list(map(int,input().split()))

    q=[]
    for x in arr:
        heapq.heappush(q,x)
    for i in range(n):
        num=heapq.heappop(q)
        for j in range(k):
            tmp=num*arr[j]
            heapq.heappush(q,tmp)

            if num%arr[j]==0:
                break
    else:
        print(num)