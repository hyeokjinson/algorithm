import heapq

if __name__ == '__main__':
    n,k=map(int,input().split())

    arr=[]

    for i in range(n):
        m,v=map(int,input().split())
        heapq.heappush(arr,[m,v])

    bag=[int(input())for _ in range(k)]
    bag.sort()

    q=[]
    res=0

    for i in range(k):
        now=bag[i]

        while arr and now>=arr[0][0]:
            m,v=heapq.heappop(arr)
            heapq.heappush(q,-v)

        if q:
            res-=heapq.heappop(q)
        elif not arr:
            break
    print(res)