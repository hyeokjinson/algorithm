def findOdd(series):
    distance = []
    res = ""

    for s in series:
        dist = []
        for i in range(len(s)-1):
            dist.append(ord(s[i+1]) - ord(s[i]))
        distance.append(tuple(dist))

    for i in range(len(distance)):
        if distance.count(distance[i]) == 1:
            res = series[i]
            break

    return res

##https://neptuneworld.in/blog/identifying-odd-one-out-series-strings-hackerrank/

def getPotentialDomains(n: int):
    lines = list()

    res = list()
    for i in range(0, n):
        l = input("enter line {}: ".format(i))
    lines.append(l)

    for j in lines:
        m = j.split(" ")
    for x in m:
        if "http://" in x or "https://" in x:
            res.append((x.split("//")[1]).split("/")[0])

    res = [r.replace("www.", "") for r in res]
    res = [r.replace("web.", "") for r in res]

    x = ''
    for item in res:
        x = x + str(item) + ";"

    return x


def getPotentialDomains(n: int):
    lines = list()


    res = list()
    for i in range(0, n):
        l = input("enter line {}: ".format(i))
    lines.append(l)

    for j in lines:
        m = j.split(" ")
    for x in m:
        if "http://" in x or "https://" in x:
            res.append((x.split("//")[1]).split("/")[0])

    res = [r.replace("www.", "") for r in res]
    res = [r.replace("web.", "") for r in res]

    x = ''
    for item in res:
        x = x + str(item) + ";"

    return x

print("Output: {}".format(getPotentialDomains(n=4)))