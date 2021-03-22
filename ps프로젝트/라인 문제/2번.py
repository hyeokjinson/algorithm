def check1(inp_str):
    if 8<=len(inp_str)<=15:
        return True
    return False

def check2(inp_str):
    arr=['~','!','@','#','$','%','^','&','*']

    for x in inp_str:
        if x.isdigit():
            continue
        elif x.isalpha():
            continue
        elif x in arr:
            continue
        else:
            return False
    return True
def check3(inp_str):
    arr=[0]*4

    for x in inp_str:
        if x.isdigit():
            arr[0]=1
        elif x.isalpha():
            if x==x.lower():
                arr[1]=1
            else:
                arr[2]=1
        elif x in arr:
            arr[3]=1
    if sum(arr)>=3:
        return True

    return False

def check4(inp_str):
    stack=[]

    for i in range(len(inp_str)-4):
        temp=''
        temp+=inp_str[i]*4
        if inp_str[i:i+4]==temp:
            return False
    return True

def check5(inp_str):
    dic={}
    for x in inp_str:
        if x not in dic:
            dic[x]=1
        else:
            dic[x]+=1
    for key,value in dic.items():
        if value>=5:
            return False
    return True

def solution(inp_str):
    answer = []
    cnt=1
    if not check1(inp_str):
        answer.append(cnt)
    cnt+=1
    if not check2(inp_str):
        answer.append(cnt)
    cnt+=1
    if not check3(inp_str):
        answer.append(cnt)
    cnt+=1
    if not check4(inp_str):
        answer.append(cnt)
    cnt+=1
    if not check5(inp_str):
        answer.append(cnt)


    if len(answer)==0:
        answer.append(0)
    return answer
inp_str="ZzZz9Z824"

print(solution(inp_str))