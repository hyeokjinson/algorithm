from collections import deque
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
q=deque(range(1,n+1))
res=[]
while q:
    q.rotate(-m+1)
    res.append(str(q.popleft()))
print('<%s>'%(', '.join(res)))