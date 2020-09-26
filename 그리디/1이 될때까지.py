n,k=map(int,input().split())
cnt=0
while True:
    if n==1:
        print(cnt)
        break
    if n//k!=0:
        n=n//k
        cnt+=1
    else:
        n-=1
        cnt+=1