n=int(input())
arr1=list(map(int,input().split()))
m=int(input())
arr2=list(map(int,input().split()))
p1=p2=0
c=[]
while p1<n and p2<m:
    if arr1[p1]<=arr2[p2]:
        c.append(arr1[p1])
        p1+=1
    else:
        c.append(arr2[p2])
        p2+=1
if p1<n:
    c=c+arr1[p1:]
if p2<m:
    c=c+arr2[p2:]

for x in c:
    print(x,end=' ')