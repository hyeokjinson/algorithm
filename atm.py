n=int(input())
p=list(map(int,input().split()))
result=[]
su=0
p.sort()
for i in range(n):
    su+=p[i]
    result.append(su)

print(sum(result))