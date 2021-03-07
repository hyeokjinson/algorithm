import sys

def dfs(L,seq):
    for j in range(1,L//2+1):
        if seq[L-(2*j):L-(2*j)+j]==seq[L-(2*j)+j:]:
            return
    if L==n:
        for x in seq:
            print(x,end='')
        sys.exit(0)


    for i in range(1,4):
        if seq and seq[-1]==i:
            continue

        dfs(L+1,seq+[i])

if __name__ == '__main__':
    n=int(input())
    dfs(0,[])