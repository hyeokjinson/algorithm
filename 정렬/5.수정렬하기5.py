import heapq
import sys

input=sys.stdin.readline
if __name__ == '__main__':
    n=int(input())
    q=[]

    for _ in range(n):
        heapq.heappush(q,int(input()))

    while q:
        print(heapq.heappop(q))
