s=input()
tmp=[]
sum_=0
for x in s:
    if x.isdigit():
        sum_+=int(x)
    else:
        tmp.append(x)
tmp.sort()
if sum_!=0:
    tmp.append(str(sum_))
print(''.join(tmp))