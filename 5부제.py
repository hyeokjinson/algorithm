n=int(input())
cnt=0
k=list(map(int,input().split()))
for i in range(5):
    if n==k[i]:
        cnt=cnt+1

print(cnt)