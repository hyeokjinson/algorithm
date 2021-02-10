if __name__ == '__main__':
    n=int(input())
    p=list(map(int,input().split()))

    sum_=0
    res=[]
    p.sort()
    for i in range(n):
        sum_+=p[i]
        res.append(sum_)
    print(sum(res))