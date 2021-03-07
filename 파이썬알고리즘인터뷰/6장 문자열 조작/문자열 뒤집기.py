if __name__ == '__main__':
    s=list(map(str,input()))

    lt=0
    rt=len(s)-1

    while lt<rt:
        s[lt],s[rt]=s[rt],s[lt]
        lt+=1
        rt-=1
    print(s)