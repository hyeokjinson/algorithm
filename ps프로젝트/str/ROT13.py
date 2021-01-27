if __name__ == '__main__':
    s=input()
    tmp=''
    for x in s:
        if x==' ':
            tmp+=' '
        elif x.isdigit():
            tmp+=x
        elif x==x.upper():
            if 65<=ord(x)+13<=90:
                tmp+=chr(ord(x)+13)
            else:
                tmp+=chr(ord(x)+13-90+64)
        elif x==x.lower():
            if 97<=ord(x)+13<=122:
                tmp+=chr(ord(x)+13)
            else:
                tmp+=chr(ord(x)+13-122+96)



    print(tmp)