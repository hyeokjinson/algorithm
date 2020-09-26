n=int(input())
dic=dict()
for i in range(n):
    word=input()
    dic[word]=1
for i in range(n-1):
    word=input()
    dic[word]=0
for key,value in dic.items():
    if value==1:
        print(key)
        break
