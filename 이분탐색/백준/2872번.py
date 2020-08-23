n=int(input())
a=[]
for _ in range(n):
    a.append(int(input()))

here=n
for i in range(n-1,-1,-1):
    if a[i]==here:
        here-=1
print(here)