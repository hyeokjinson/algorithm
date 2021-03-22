def flag_check(program,flag_rules):
    flag_rule={}

    for i in range(len(flag_rules)):
        rule=list(flag_rules[i].split())
        rule1,rule2=str(rule[0]),str(rule[1])

        flag_rule[rule1]=rule2
    return flag_rule

def check(flag_rules,com1,val):
    if flag_rules[com1]=='NUMBER':
        if val.isdigit():
            return True
        else:
            return False
    elif flag_rules[com1]=='STRING':
        if val.isalpha():
            return True
        else:
            return False
    elif flag_rules[com1]=="NULL":
        if val==None:
            return True
        else:
            return False

    return False

def solution(program, flag_rules, commands):
    answer = []
    flag_rules=flag_check(program,flag_rules)


    for command in commands:
        temp=list(map(str,command.split()))
        program_command=temp[0]
        if program_command!= program:
            answer.append(False)
            continue
        temp=temp[1:]
        flag=True

        for i in range(len(temp)):
            if temp[i] in flag_rules.keys():
                if flag_rules[temp[i]]!="NULL":
                    if not check(flag_rules,temp[i],temp[i+1]):
                        flag=False
                else:
                    if i+1<len(temp) and temp[i+1] not in flag_rules.keys():
                        flag=False
                        break
            else:
                if i%2==0:
                    flag=False

        answer.append(flag)
    return answer
program="line"
flag_rules=	["-s STRING", "-n NUMBER", "-e NULL"]
flag_rules=["-s STRING", "-n NUMBER", "-e NULL"]
command=["line -n 100 -s hi -e", "lien -s Bye"]
#command=["line -s 123 -n HI", "line fun"]
print(solution(program,flag_rules,command))