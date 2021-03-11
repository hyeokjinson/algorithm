if __name__ == '__main__':
    n,m=map(int,input().split())
    s={}
    for _ in range(n):
        tmp=input()
        if tmp not in s:
            s[tmp]=1

    count=0
    for _ in range(m):
        s1=input()
        if s1 in s.keys():
            count+=1
    print(count)