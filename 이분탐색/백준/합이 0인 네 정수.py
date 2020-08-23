n=int(input())
a=[]
b=[]
c=[]
d=[]
res=set()
for _ in range(n):
    num1,num2,num3,num4=map(int,input().split())
    a.append(num1)
    b.append(num2)
    c.append(num3)
    d.append(num4)

ab,cd={},{}
for a_ in a:
    for b_ in b:
        if not ab.get(a_+b_):
            ab[a_+b_]=1
        else:
            ab[a_ + b_] += 1
for c_ in c:
    for d_ in d:
        if not cd.get(c_+d_):
            cd[c_+d_]=1
        else:
            cd[c_ + d_] += 1
res=0
for value,key in enumerate(ab):
    if cd.get(-key):
        res+=ab[key]*cd[-key]
print(res)