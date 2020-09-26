n=int(input())
res=[]
for i in range(n):
    s,e=map(int,input().split())
    res.append((s,e))
res.sort(key=lambda x:(x[1],x[0]))
ep=0
cnt=0
for s,e in res:
    if s>=ep:
        ep=e
        cnt+=1
print(cnt)