def make_table(pattern):
    l=len(pattern)
    table=[0]*l
    j=0
    for i in range(1,l):
        while j>0 and pattern[i]!=pattern[j]:
            j=table[j-1]
        if pattern[i]==pattern[j]:
            j+=1
            table[i]=j
    return table

if __name__ == '__main__':
    while True:
        s=input()
        if s=='.':
            break
        table=make_table(s)

        if len(s)%(len(s)-table[-1])!=0:
            print(1)
        else:
            print(len(s)//(len(s)-table[-1]))
