s=input()
data=int(s[0])
for i in range(1,len(s)):
    num=int(s[i])
    if data<=1 or num<=1:
        data+=num
    else:
        data*=num

print(data)