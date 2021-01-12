from collections import deque

n,m=map(int,input().split())
arr=list(map(int,input().split()))
q=deque(range(1,n+1))
res=0

for idx in range(len(arr)):
    if arr[idx]==q[0]:
        q.popleft()
        continue
    q_idx=q.index(arr[idx])

    if q_idx>len(q)//2:
        q.rotate(len(q)-q_idx)
        res+=len(q)-q_idx
    elif q_idx<=len(q)//2:
        q.rotate(-q_idx)
        res+=q_idx
    q.popleft()
print(res)