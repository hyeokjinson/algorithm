n=list(map(int,input().strip()))
sum1=0
sum2=0
for i in range(len(n)//2):
    sum1+=n[i]
    sum2+=n[-i-1]
if sum1==sum2:
    print("LUCKY")
else:
    print("READY")