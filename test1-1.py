def solution(S):
    S=list(map(str,S.strip()))
    value=S.count('a')
    if value==0:
        return 2 ** len(S)
    cnt_a=0
    res=0
    print(S)
    for x in S:
        if cnt_a==3:
            return -1
        if x=='a':
            cnt_a+=1
        else:
            if cnt_a<3:
                while cnt_a<3:
                    cnt_a+=1
                    res+=1
            cnt_a=0
    return res

S='aabab'
print(solution(S))