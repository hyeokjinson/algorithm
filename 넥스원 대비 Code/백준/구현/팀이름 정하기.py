def calcu(L,O,V,E):
    return ((L+O)*(L+V)*(L+E)*(O+V)*(O+E) *(V+E))%100
if __name__ == '__main__':
    name=input()
    n=int(input())

    L=0;O=0;V=0;E=0;
    for str in name:
        if str=="L":
            L+=1
        if str=="O":
            O+=1
        if str=="V":
            V+=1
        if str=="E":
            E+=1
    # result=calcu(L,O,V,E)
    max_=-2147000
    str_=list()
    for i in range(n):
        str_.append(input())
    str_.sort()
    L_val=L;O_val=O;V_val=V;E_val=E;
    for str1 in str_:
        L_val = L;O_val = O;V_val = V;E_val = E;
        for str in str1:
            if str == "L":
                L_val += 1
            if str == "O":
                O_val += 1
            if str == "V":
                V_val += 1
            if str == "E":
                E_val+= 1
        if max_<calcu(L_val,O_val,V_val,E_val):
            result=str1
            max_=calcu(L_val,O_val,V_val,E_val)
    print(result)
