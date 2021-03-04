import sys
input=sys.stdin.readline

if __name__ == '__main__':
    check=[True]*(1000001)

    check[0]=False
    check[1]=False

    for i in range(1000001):
        if check[i]:
            for j in range(i*2,1000001,i):
                check[j]=False


    while True:
        n=int(input())
        ans1=ans2=0
        if n==0:
            break
        for i in range(3,1000001):
            if check[i]:
                if check[n-i]:
                    ans1=i
                    ans2=n-i
                    break

        if ans1==0 and ans2==0:
            print("Goldbach's conjecture is wrong.")
        else:
            print("%d = %d + %d"%(n,ans1,ans2))

