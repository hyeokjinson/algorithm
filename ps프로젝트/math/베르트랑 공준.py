if __name__ == '__main__':
    while True:
        n=int(input())
        if n==0:
            break
        check=[True]*((2*n)+1)
        check[0]=False
        check[1]=False

        for i in range(len(check)):
            if check[i]:
                for j in range(i*2,len(check),i):
                    check[j]=False
        cnt=0

        for i in range(n+1,2*n+1):
            if check[i]:
                cnt+=1
        print(cnt)
