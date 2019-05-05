def solution(participant, completion):
    dict={}
    temp=0
    for part in participant:
        dict[hash(part)]=part
        temp+=hash(part)
    for com in completion :
        temp-=hash(com)
    answer = dict[temp]
    return answer

list1=["a","b","c","a"]
list2=["a","b","c"]

print(solution(list1, list2))