def change(x):
    res=0

    for i in x:
        res=res*10+int(i)
    return res

if __name__ == '__main__':
    n=input()

    n=sorted(n,reverse=True)
    if '0' not in n:
        print(-1)
    else:
        sum_=0
        for x in n:
            sum_+=int(x)
        if sum_%3!=0:
            print(-1)
        else:
            print(change(n))

