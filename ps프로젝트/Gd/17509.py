if __name__ == '__main__':
    g=[[] for _ in range(11)]

    for i in range(11):
        g[i]=list(map(int,input().split()))

    g.sort(key=lambda x:x[1])
    g.sort(key=lambda x:x[0])

    s=0
    time=0

    for i in range(11):
        time+=g[i][0]
        s+=time+20*g[i][1]
    print(s)