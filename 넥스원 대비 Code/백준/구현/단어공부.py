if __name__ == '__main__':
    str=input()
    hash={}

    for i in range(ord("Z")-ord('A')+1):
        hash[i]=0



    for val in str:
        if val.isupper():
            hash[ord(val)-65]+=1
        elif val.islower():
            hash[ord(val)-97]+=1

    max_=-2147000
    for k in range(len(hash)):
        if(max_<hash[k]):
            max_=hash[k]
    # print(max_)
    result=""
    flag_=False
    for k in range(len(hash)):
        if hash[k]==max_:
            if flag_==False:
                result=chr(k+65)
                flag_=True
            else:
                result="?"

    print(result)


