import heapq
import sys

input=sys.stdin.readline
if __name__ == '__main__':
    t=int(input())
    q=[]
    for _ in range(t):
        n=int(input())
        if n==0:
            if not q:
                print(0)
            else:
                print(heapq.heappop(q))
        else:
            heapq.heappush(q,n)