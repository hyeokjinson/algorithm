def check_table(table_list):
    table_list=table_list.split()
    job=table_list[0]
    table_list=table_list[1:]
    scores={}
    score=5
    for x in table_list:
        scores[x]=score
        score-=1
    return job, scores


def prefer_score(language, preference):
    scores={}
    for i in range(len(language)):
        scores[language[i]]=preference[i]
    return scores


def solution(table, languages, preference):
    answer=''
    max_=-2147000000

    for i in range(len(table)):
        sum_=0
        job, table_list=check_table(table[i])

        prefer_list=prefer_score(languages, preference)

        for x in languages:
            if x not in table_list:
                temp=0
            else:

                temp=prefer_list[x] * table_list[x]
            sum_+=temp
        if sum_ >= max_:
            if sum_ == max_:
                dic=[answer, job]
                dic.sort()
                answer=dic[0]
            else:
                answer=job
            max_=sum_

    return answer