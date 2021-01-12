from itertools import combinations
s=input()
candidate=[i for i in range(1,len(s))]
combi_candi=list(combinations(candidate,2))
res='z'*len(s)
for combi in combi_candi:
    split1,split2=combi[0],combi[1]
    tmp1=s[:split1][::-1]
    tmp2=s[split1:split2][::-1]
    tmp3=s[split2:][::-1]
    tmp=tmp1+tmp2+tmp3

    if tmp<res:
        res=tmp
print(res)