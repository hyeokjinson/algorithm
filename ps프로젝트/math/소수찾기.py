if __name__ == '__main__':
    n=int(input())
    num=list(map(int,input().split()))

    answer=0

    for i in range(n):
        if num[i]>1:
            cnt=1
            for j in range(2,num[i]+1):
                if num[i]%j==0:
                    cnt+=1
            if cnt==2:
                answer+=1
    print(answer)