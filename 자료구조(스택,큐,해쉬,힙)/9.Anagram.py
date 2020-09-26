a=dict()
b=dict()

word=input()
for x in word:
    a[x]=a.get(x,0)+1
word2=input()
for x in word2:
    b[x]=b.get(x,0)+1
for i in a.keys():
    if i in b.keys():
        if a[i]!=b[i]:
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")
