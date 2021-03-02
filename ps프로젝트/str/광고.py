def solve(pattern):
    table=[0]*l
    j=0

    for i in range(1,l):
        while j>0 and pattern[i]!=pattern[j]:
            j=table[j-1]
        if pattern[i]==pattern[j]:
            j+=1
            table[i]=j
    return l-table[l-1]

if __name__ == '__main__':
    l=int(input())
    s=input()
    print(solve(s))