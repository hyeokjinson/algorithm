n=int(input())
max=-10000000
for _ in range(n):
    tmp=input().split()
    tmp.sort()
    a,b,c=map(int,tmp)
    if a==b and b==c:
        value=10000+a*1000
    elif a==b or a==c:
        value=10000+a*100
    elif b==c:
        value=10000+b*100
    else:
        value=c*100
    if value>max:
        max=value
print(max)