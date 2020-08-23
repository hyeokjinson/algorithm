n=int(input())
a=list(map(int,input().split()))
tmp=""
lt=0
rt=n-1
last=0
m=[]
while lt<=rt:
    if a[lt]>last:
        m.append((a[lt],'L'))
    if a[rt]>last:
        m.append((a[rt],'R'))
    m.sort()

    if len(m)==0:
        break
    else:
        tmp=tmp+m[0][1]
        last=m[0][0]
        if m[0][1]=='L':
            lt+=1
        else:
            rt-=1
    m.clear()

print(len(tmp))
print(tmp)
