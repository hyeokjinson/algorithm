import heapq
import sys
input=sys.stdin.readline
if __name__ == '__main__':
    n=int(input())
    q=[]
    for x in map(int,input().split()):
        heapq.heappush(q,x)

    for _ in range(1,n):
        for x in map(int,input().split()):
            heapq.heappush(q,x)
            heapq.heappop(q)
            print(q)
    print(heapq.heappop(q))
