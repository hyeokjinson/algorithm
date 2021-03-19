if __name__ == '__main__':
    n=int(input())
    weight=list(map(int,input().split()))
    res=0

    weight.sort()

    for x in weight:
        if res+1>=x:
            res+=x
        else:
            break
    print(res+1)