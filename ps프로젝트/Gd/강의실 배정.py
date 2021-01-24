import sys
import heapq
input=sys.stdin.readline

if __name__ == '__main__':
    n=int(input())

    arr=[]

    for _ in range(n):
        s,e=map(int,input().split())
        arr.append((s,e))

    arr.sort(key=lambda x:(x[0],x[1]))

    print(arr)

    q=[]
    heapq.heappush(q,arr[0][1])
    for i in range(1,n):
        if q[0]<=arr[i][0]:
            heapq.heappop(q)
        heapq.heappush(q,arr[i][1])
    print(len(q))