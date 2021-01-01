if __name__ == '__main__':
    c=[0]*10001
    n=int(input())
    for i in range(n):
        tmp=int(input())
        c[tmp]+=1

    for i in range(10001):
        if c[i]:
            for j in range(c[i]):
                print(i)