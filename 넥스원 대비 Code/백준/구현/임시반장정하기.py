if __name__ == '__main__':
    n=int(input())
    map_=[list(map(int,input().split()))for _ in range(n)]
    cnt=[0]*n

    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            for k in range(5):
                if map_[i][k]==map_[j][k]:
                    cnt[i]+=1
                    break

    print(cnt.index(max(cnt))+1)
