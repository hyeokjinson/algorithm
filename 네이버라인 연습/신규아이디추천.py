def check1(new_id):
    return new_id.lower()

def check2(new_id):
    ans=''
    arr=['-','_','.']
    for x in new_id:
        if x.isalpha():
            ans+=x
        elif x.isdigit():
            ans+=x
        elif x in arr:
            ans+=x
    print(ans)
    return ans

def check3(new_id):
    new_id=list(new_id)
    if len(new_id)==0:
        return ''
    stack=[]
    for i in range(len(new_id)):
        if new_id[i]=='.':
            if stack and stack[-1]=='.':
                continue
            else:
                stack.append(new_id[i])
        else:
            stack.append(new_id[i])
    print(''.join(stack))
    return ''.join(stack)

def check4(new_id):

    new_id=list(new_id)
    n=len(new_id)
    if n>0 and new_id[0]=='.':
        new_id.pop(0)
    n=len(new_id)
    if n>0 and new_id[-1]=='.':
        new_id.pop()

    return ''.join(new_id)

def check5(new_id):
    if len(new_id)==0:
        return 'a'
    return new_id
def check6(new_id):

    if len(new_id)==0:
        return ''
    if len(new_id)>=16:
        new_id=list(new_id[:15])
        if new_id[-1]=='.':
            return ''.join(new_id[:14])
        else:
            return ''.join(new_id)
    else:
        return ''.join(new_id)

def check7(new_id):
    count=len(new_id)

    while count<3:
        new_id+=new_id[-1]
        count+=1
    return new_id


def solution(new_id):
    answer=check1(new_id)
    answer=check2(answer)
    answer=check3(answer)
    answer=check4(answer)
    answer=check5(answer)
    answer=check6(answer)
    answer=check7(answer)

    return answer

print(solution("z-+.^."))
