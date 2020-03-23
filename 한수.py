n=int(input())

if n<100:
    print(n)
else:
    cnt=99
    for i in range(100,n+1):
        hund=i//100
        ten=(i%100)//10
        num=i%10
        if (hund-ten)==(ten-num):
            cnt+=1
print(cnt)