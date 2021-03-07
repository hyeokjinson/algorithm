def expand(left,right):
    while left>=0 and right<=len(s) and s[left]==s[right-1]:
        left-=1
        right+=1
    if len(s)<2 or s==s[::-1]:
        return s

    return s[left+1:right-1]

if __name__ == '__main__':
    s = "babad"
    res=''

    for i in range(len(s)-1):
        res=max(res,expand(i,i+1),expand(i,i+2),key=len)

    print(res)