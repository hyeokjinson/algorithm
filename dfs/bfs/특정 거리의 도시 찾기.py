from _collections import deque

n,m,k,x=map(int,input().split())
arr=[[] for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    arr[a].append(b)

dis=[-1]*(n+1)
dis[x]=0
q=deque([x])

while q:
    tmp=q.popleft()
    for next_value in arr[tmp]:
        if dis[next_value]==-1:
            dis[next_value]=dis[tmp]+1
            q.append(next_value)

check=False

for i in range(1,n+1):
    if dis[i]==k:
        print(i)
        check=True
if check==False:
    print(-1)