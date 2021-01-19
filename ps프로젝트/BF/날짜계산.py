if __name__ == '__main__':
    e,s,m=map(int,input().split())

    cnt=1
    c1=c2=c3=1
    while True:
        if c1==e and c2==s and c3==m:
            break
        c1+=1
        c2+=1
        c3+=1

        if c1==16:
            c1=1
        if c2==29:
            c2=1
        if c3==20:
            c3=1
        cnt+=1

    print(cnt)

