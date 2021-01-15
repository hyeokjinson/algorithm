import heapq
import sys
input=sys.stdin.readline
if __name__ == '__main__':
    n=int(input())
    q=[]
    res=0

    for _ in range(n):
        heapq.heappush(q,int(input()))

    while len(q)!=1:
        num1=heapq.heappop(q)
        num2=heapq.heappop(q)
        res+=num1+num2
        heapq.heappush(q,num1+num2)
    print(res)