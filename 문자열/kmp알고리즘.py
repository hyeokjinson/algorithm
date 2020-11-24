def computeLPS(pat,lps):
    leng=0

    i=1

    while i<len(pat):
        if pat[i]==pat[leng]:
            leng+=1
            lps[i]=leng
            i+=1
        else:
            if leng!=0:
                leng=lps[leng-1]
            else:
                lps[i]=0
                i+=1

def KMPSearch(pat,txt):
    M=len(pat)
    N=len(txt)

    lps=[0]*M

    computeLPS(pat,lps)

    i=0
    j=0

    while i<N:
        if pat[j]==txt[i]:
            i+=1
            j+=1

        elif pat[j]!=txt[i]:

            if j!=0:
                j=lps[j-1]
            else:
                i+=1

        if j==M:
            j=lps[j-1]
            return True

if __name__ == '__main__':
    s=input()
    p=input()

    if KMPSearch(p,s):
        print(1)
    else:
        print(0)