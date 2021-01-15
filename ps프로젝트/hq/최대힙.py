import heapq
import sys
input=sys.stdin.readline

if __name__ == '__main__':
    n=int(input())
    q=[]

    for _ in range(n):
        tmp=int(input())
        if tmp==0:
            if not q:
                print(0)
            else:
                print(-heapq.heappop(q))
        else:
            heapq.heappush(q,-tmp)