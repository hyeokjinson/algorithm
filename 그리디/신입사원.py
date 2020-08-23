T=int(input())
res=[]
for _ in range(T):
    n=int(input())
    score=[]
    cnt=0
    for i in range(n):
        a,b=map(int,input().split())
        score.append((a,b))
    score.sort()
    largest=217000000

    for x,y in score:
        if y<largest:
            largest=y
            cnt+=1
    res.append(cnt)

for x in res:
    print(x)