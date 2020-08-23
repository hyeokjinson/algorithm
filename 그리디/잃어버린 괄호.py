res=0
a=input().split('-')
for i in a[0].split('+'):
    res+=int(i)

for i in a[1:]:
    for j in i.split('+'):
        res-=int(j)
print(res)