from _collections import deque
n,k=map(int,input().split())
res=[i for i in range(1,n+1)]
des=deque(res)
for i in range(n):
    cnt=1
    while k!=cnt:
        node=des.popleft()
        des.append(node)
        cnt+=1
    n=des.popleft()
print(n)
