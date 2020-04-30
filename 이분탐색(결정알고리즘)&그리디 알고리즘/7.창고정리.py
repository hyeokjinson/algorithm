L=int(input())
a=list(map(int,input().split()))
m=int(input())
a.sort()
for i in range(m):
    a[0]=a[0]+1
    a[-1]=a[-1]-1
    a.sort()

print(a[-1]-a[0])