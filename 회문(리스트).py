arr=list("A man, a plan, a canal - Panama")
des=[]
for val in arr:
    if val.isalpha():
        des.append(val)

cnt=int(len(des)/2)

left=[des[x].lower() for x in range(0,cnt)]
right=[des[-x].lower() for x in range(1,cnt+1)]

if left==right:
    print("회문")
else:
    print("회문 x")