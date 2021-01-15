from collections import deque
import sys
input=sys.stdin.readline
if __name__ == '__main__':
    n,k=map(int,input().split())
    cnt=0
    arr=[[]for _ in range(22)]
    q=deque(arr)

    for i in range(n):
        s=input()

        length=len(s)
        while len(q[length])!=0 and i-q[length][0]>k:
            q[length].pop(0)
        cnt+=len(q[length])
        q[length].append(i)
    print(cnt)
