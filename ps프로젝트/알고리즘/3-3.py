def flag_check(program, flag_rules):
    flag_rule={}

    for i in range(len(flag_rules)):
        rule=list(flag_rules[i].split())
        rule1, rule2=str(rule[0]), str(rule[1])

        flag_rule[rule1]=rule2
    return flag_rule


def check(flag_rules, com1, val):
    if flag_rules[com1] == 'NUMBER':
        if val.isdigit():
            return True
        else:
            return False
    elif flag_rules[com1] == 'STRING':
        if val.isalpha():
            return True
        else:
            return False
    elif flag_rules[com1] == "NULL":
        if val == None:
            return True
        else:
            return False

    return False


def check2(flag_rules, com1):
    s=[]
    while com1:
        now=com1.pop(0)
        if now in flag_rules.keys():
            break
        s.append(now)

    for x in s:
        if not x.isdigit():
            return False
    return True


def check3(flag_rules, com1):
    s=[]
    com1=list(com1)
    while com1:
        now=com1.pop(0)
        if now in flag_rules.keys():
            break
        s.append(now)

    for x in s:
        if not x.isalpha():
            return False
    return True


def check4(flag_rules, com1):
    s=[]
    com1=list(com1)
    while com1:
        now=com1.pop(0)
        if now in flag_rules.keys():
            break
        s.append(now)
    if len(s) > 1:
        return False
    for x in s:
        if not x.isalpha():
            return False
    return True


def solution(program, flag_rules, commands):
    answer=[]
    flag_rules=flag_check(program, flag_rules)

    for command in commands:
        temp=list(map(str, command.split()))

        program_command=temp[0]
        if program_command != program:
            answer.append(False)
            continue
        temp=[temp[i] for i in range(1, len(temp))]
        flag=True

        for i in range(len(temp)):

            if temp[i] in flag_rules.keys():
                # print(temp[i+1:])
                if flag_rules[temp[i]] != "NULL":

                    if flag_rules[temp[i]] == "NUMBERS":

                        if not check2(flag_rules, temp[i + 1:]):

                            flag=False
                            break
                        else:
                            continue

                    elif flag_rules[temp[i]] == "STRINGS":

                        if not check3(flag_rules, temp[i + 1:]):
                            flag=False
                            break
                        else:
                            continue
                    elif flag_rules[temp[i]] == "STRING":
                        if not check4(flag_rules, temp[i + 1:]):
                            flag=False
                            break
                        else:
                            continue


                    elif not check(flag_rules, temp[i], temp[i + 1]):
                        flag=False
                        break
                    elif i + 1 < len(temp) and temp[i + 1] not in flag_rules.keys():

                        flag=False
                        break
            # else:
            #     if i%2==0:
            #         flag=False

        answer.append(flag)
    return answer