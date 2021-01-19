if __name__ == '__main__':
    n=int(input())
    m=int(input())

    total_num={str(i) for i in range(0,10)}

    if m==0:
        pass
    else:
        binary_num=set(input().split())
        total_num-=binary_num

    res=abs(n-100)
    for i in range(1000001):

        flag=False

        for part_num in str(i):
            if part_num not in total_num:
                flag=True
                break
        if not flag:
            res=min(res,abs(n-i)+len(str(i)))
    print(res)
