dict={}
def solution(record):
    for i in record:
        a = i.split(' ')
        if a in "Change" or "Enter":
            dict[a[1]]= a[2]


    answer = []
    return answer

list = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
