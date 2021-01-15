import heapq
import sys

input=sys.stdin.readline
if __name__ == '__main__':
    n=int(input())
    max_q=[]
    min_q=[]
    for _ in range(n):
        num=int(input())
        if not max_q:
            heapq.heappush(max_q,-num)
        elif len(max_q)==len(min_q):
            heapq.heappush(max_q,-num)
        else:
            heapq.heappush(min_q,num)

        if max_q and min_q and -max_q[0]>=min_q[0]:
            a=heapq.heappop(max_q)
            b=heapq.heappop(min_q)

            heapq.heappush(max_q,-b)
            heapq.heappush(min_q,-a)

        print(-max_q[0])



