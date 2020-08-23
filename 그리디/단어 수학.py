n=int(input())
word=[]
for _ in range(n):
    tmp=input()
    word.append(list(tmp))
num=[i for i in range(9,-1,-1)]
dic={}
for i in range(n):
    for j in range(len(word[i])):
        if word[i][j] not in dic:
            dic[word[i][j]]=pow(10,len(word[i])-j-1)
        else:
            dic[word[i][j]]+=pow(10,len(word[i])-j-1)
dic=sorted(dic.items(),reverse=True,key=lambda item:item[1])
res=0
for x,y in dic:
    res+=num.pop(0)*y
print(res)