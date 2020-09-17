import copy

s1=list(input())
s2=list(input())
dy=[['']*(len(s2)+1) for _ in range(len(s1)+1)]
for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        if s1[i-1]==s2[j-1]:
            dy[i][j]=dy[i-1][j-1]+s1[i-1]
        else:
            if len(dy[i-1][j])>=len(dy[i][j-1]):
                dy[i][j]=dy[i-1][j]
            else:
                dy[i][j]=dy[i][j-1]

if len(dy[-1][-1])==0:
    print(0)
else:
    print(len(dy[-1][-1]))
    print(dy[-1][-1])
