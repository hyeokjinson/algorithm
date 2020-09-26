n=int(input())

for i in range(n):
    a=input()
    a=a.upper()
    cnt=(len(a)//2)
    for j in range(cnt):
        if a[j]!=a[-1-j]:
            print("#%d No"%(i+1))
            break
    else:
        print("#%d Yes"%(i+1))


#s[::-1]->리버스 시켜주는 구문
